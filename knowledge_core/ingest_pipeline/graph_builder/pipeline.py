from __future__ import annotations

import argparse
import json
import logging
import math
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence
from urllib import request

import psycopg2
import psycopg2.extras

from knowledge_core.ingest_pipeline.posts import PostExtracted, extract_publish_posts


logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class EmbeddingConfig:
    model: str
    batch_size: int
    provider: str
    normalize_text: bool = True


@dataclass(frozen=True)
class GraphConfig:
    k: int
    min_similarity: float
    method: str = "topk"
    doc_type: str = "post"


@dataclass(frozen=True)
class DbConfig:
    dsn: str


@dataclass(frozen=True)
class ExecutionConfig:
    mode: str
    limit_posts: int | None


@dataclass(frozen=True)
class PipelineConfig:
    embeddings: EmbeddingConfig
    graph: GraphConfig
    execution: ExecutionConfig


@dataclass(frozen=True)
class EmbeddingRecord:
    doc_id: str
    source_hash: str
    vector: list[float]


class EmbeddingProvider:
    def __init__(self, model: str, batch_size: int) -> None:
        self.model = model
        self.batch_size = batch_size

    def embed_texts(self, texts: Sequence[str]) -> list[list[float]]:
        raise NotImplementedError


class OpenAIEmbeddingProvider(EmbeddingProvider):
    def __init__(self, model: str, batch_size: int, api_key: str) -> None:
        super().__init__(model, batch_size)
        if not api_key:
            raise ValueError("OPENAI_API_KEY не задан")
        self._api_key = api_key

    def embed_texts(self, texts: Sequence[str]) -> list[list[float]]:
        payload = {
            "model": self.model,
            "input": list(texts),
        }
        data = json.dumps(payload).encode("utf-8")
        req = request.Request(
            "https://api.openai.com/v1/embeddings",
            data=data,
            method="POST",
            headers={
                "Authorization": f"Bearer {self._api_key}",
                "Content-Type": "application/json",
            },
        )
        with request.urlopen(req, timeout=60) as response:
            body = response.read()
        parsed = json.loads(body)
        if "data" not in parsed:
            raise RuntimeError(f"Некорректный ответ OpenAI: {parsed}")
        return [item["embedding"] for item in parsed["data"]]


def run_pipeline(
    source_root: Path,
    db_config: DbConfig,
    embedding_config: EmbeddingConfig,
    graph_config: GraphConfig,
    execution_config: ExecutionConfig,
    full_rebuild: bool,
) -> None:
    posts = extract_publish_posts(source_root)
    posts = apply_limit(posts, execution_config.limit_posts)
    logger.info("Найдено publish-постов: %s", len(posts))

    provider = build_provider(embedding_config)
    normalized_texts = {
        post.id: normalize_text(post.text_for_embedding)
        if embedding_config.normalize_text
        else post.text_for_embedding
        for post in posts
    }

    with psycopg2.connect(db_config.dsn) as conn:
        conn.autocommit = False
        existing = fetch_existing_embeddings(
            conn,
            doc_ids=[post.id for post in posts],
            doc_type=graph_config.doc_type,
            model=embedding_config.model,
        )

        embeddings = build_embeddings(
            provider,
            posts=posts,
            normalized_texts=normalized_texts,
            existing=existing,
            doc_type=graph_config.doc_type,
            model=embedding_config.model,
            conn=conn,
        )

        if full_rebuild or execution_config.mode == "full":
            clear_edges(conn, graph_config)

        edges = build_similarity_edges(embeddings, graph_config)
        persist_edges(
            conn,
            edges,
            graph_config=graph_config,
            affected_doc_ids={record.doc_id for record in embeddings},
            full_rebuild=full_rebuild,
        )

        conn.commit()


def build_provider(config: EmbeddingConfig) -> EmbeddingProvider:
    provider = config.provider.lower()
    if provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY", "")
        return OpenAIEmbeddingProvider(config.model, config.batch_size, api_key)
    raise ValueError(f"Неизвестный провайдер embeddings: {config.provider}")


def normalize_text(text: str) -> str:
    lowered = text.lower()
    normalized = re.sub(r"\s+", " ", lowered).strip()
    return normalized


def fetch_existing_embeddings(
    conn: psycopg2.extensions.connection,
    doc_ids: list[str],
    doc_type: str,
    model: str,
) -> dict[str, EmbeddingRecord]:
    if not doc_ids:
        return {}

    query = """
        SELECT doc_id::text, source_hash, embedding::text
        FROM knowledge.embeddings
        WHERE doc_type = %s AND model = %s AND doc_id = ANY(%s)
    """
    with conn.cursor() as cur:
        cur.execute(query, (doc_type, model, doc_ids))
        rows = cur.fetchall()

    records: dict[str, EmbeddingRecord] = {}
    for doc_id, source_hash, embedding_text in rows:
        vector = parse_pgvector_text(embedding_text)
        records[str(doc_id)] = EmbeddingRecord(
            doc_id=str(doc_id),
            source_hash=source_hash,
            vector=vector,
        )
    return records


def build_embeddings(
    provider: EmbeddingProvider,
    posts: list[PostExtracted],
    normalized_texts: dict[str, str],
    existing: dict[str, EmbeddingRecord],
    doc_type: str,
    model: str,
    conn: psycopg2.extensions.connection,
) -> list[EmbeddingRecord]:
    to_update: list[PostExtracted] = []
    embeddings: list[EmbeddingRecord] = []

    for post in posts:
        record = existing.get(post.id)
        if record and record.source_hash == post.source_hash:
            embeddings.append(record)
            continue
        to_update.append(post)

    for batch in chunked(to_update, provider.batch_size):
        texts = [normalized_texts[item.id] for item in batch]
        vectors = provider.embed_texts(texts)
        if len(vectors) != len(batch):
            raise RuntimeError("Количество embeddings не совпадает с количеством документов")

        updated_records = []
        for post, vector in zip(batch, vectors, strict=True):
            record = EmbeddingRecord(
                doc_id=post.id,
                source_hash=post.source_hash,
                vector=vector,
            )
            embeddings.append(record)
            updated_records.append(record)

        upsert_embeddings(
            conn,
            updated_records,
            doc_type=doc_type,
            model=model,
        )

    return embeddings


def upsert_embeddings(
    conn: psycopg2.extensions.connection,
    records: list[EmbeddingRecord],
    doc_type: str,
    model: str,
) -> None:
    if not records:
        return

    values = [
        (
            record.doc_id,
            doc_type,
            model,
            record.source_hash,
            pgvector_literal(record.vector),
        )
        for record in records
    ]
    query = """
        INSERT INTO knowledge.embeddings (doc_id, doc_type, model, source_hash, embedding, updated_at)
        VALUES %s
        ON CONFLICT (doc_id, doc_type, model)
        DO UPDATE SET
            source_hash = EXCLUDED.source_hash,
            embedding = EXCLUDED.embedding,
            updated_at = now()
    """
    with conn.cursor() as cur:
        psycopg2.extras.execute_values(
            cur,
            query,
            values,
            template="(%s, %s, %s, %s, %s::vector, now())",
        )


def build_similarity_edges(
    embeddings: list[EmbeddingRecord],
    graph_config: GraphConfig,
) -> list[tuple[str, str, float]]:
    vectors = {record.doc_id: normalize_vector(record.vector) for record in embeddings}
    doc_ids = list(vectors.keys())
    candidates: dict[str, list[tuple[str, float]]] = {doc_id: [] for doc_id in doc_ids}

    for i, doc_id in enumerate(doc_ids):
        vec_a = vectors[doc_id]
        for other_id in doc_ids[i + 1 :]:
            vec_b = vectors[other_id]
            similarity = cosine_similarity(vec_a, vec_b)
            if similarity < graph_config.min_similarity:
                continue
            candidates[doc_id].append((other_id, similarity))
            candidates[other_id].append((doc_id, similarity))

    normalized_edges: dict[tuple[str, str], float] = {}
    for doc_id, edges in candidates.items():
        edges.sort(key=lambda item: item[1], reverse=True)
        for other_id, weight in edges[: graph_config.k]:
            source_id, target_id = sorted((doc_id, other_id))
            current = normalized_edges.get((source_id, target_id))
            normalized_edges[(source_id, target_id)] = max(current, weight) if current is not None else weight

    pruned_edges = prune_edges(
        [(a, b, weight) for (a, b), weight in normalized_edges.items()],
        graph_config.k,
    )
    return pruned_edges


def prune_edges(edges: list[tuple[str, str, float]], k: int) -> list[tuple[str, str, float]]:
    adjacency: dict[str, list[tuple[str, str, float]]] = {}
    for a, b, weight in edges:
        adjacency.setdefault(a, []).append((a, b, weight))
        adjacency.setdefault(b, []).append((a, b, weight))

    active_edges = {(a, b, weight) for a, b, weight in edges}

    updated = True
    while updated:
        updated = False
        for node, node_edges in list(adjacency.items()):
            if len(node_edges) <= k:
                continue
            node_edges.sort(key=lambda item: item[2])
            while len(node_edges) > k:
                edge = node_edges.pop(0)
                if edge in active_edges:
                    active_edges.remove(edge)
                    updated = True
                for endpoint in (edge[0], edge[1]):
                    if endpoint == node:
                        continue
                    adjacency[endpoint] = [
                        item for item in adjacency.get(endpoint, []) if item != edge
                    ]
    return list(active_edges)


def persist_edges(
    conn: psycopg2.extensions.connection,
    edges: list[tuple[str, str, float]],
    graph_config: GraphConfig,
    affected_doc_ids: set[str],
    full_rebuild: bool,
) -> None:
    if not full_rebuild and affected_doc_ids:
        delete_edges_for_docs(conn, graph_config, affected_doc_ids)

    if not edges:
        return

    values = [
        (
            source_id,
            target_id,
            graph_config.doc_type,
            weight,
            graph_config.method,
            graph_config.k,
            graph_config.min_similarity,
        )
        for source_id, target_id, weight in edges
    ]
    query = """
        INSERT INTO knowledge.similarity_edges
          (source_id, target_id, doc_type, weight, method, k, min_similarity, updated_at)
        VALUES %s
        ON CONFLICT (source_id, target_id, doc_type, method)
        DO UPDATE SET
          weight = EXCLUDED.weight,
          k = EXCLUDED.k,
          min_similarity = EXCLUDED.min_similarity,
          updated_at = now()
    """
    with conn.cursor() as cur:
        psycopg2.extras.execute_values(cur, query, values)


def delete_edges_for_docs(
    conn: psycopg2.extensions.connection,
    graph_config: GraphConfig,
    doc_ids: set[str],
) -> None:
    query = """
        DELETE FROM knowledge.similarity_edges
        WHERE doc_type = %s
          AND method = %s
          AND (source_id = ANY(%s) OR target_id = ANY(%s))
    """
    with conn.cursor() as cur:
        cur.execute(query, (graph_config.doc_type, graph_config.method, list(doc_ids), list(doc_ids)))


def clear_edges(
    conn: psycopg2.extensions.connection,
    graph_config: GraphConfig,
) -> None:
    query = """
        DELETE FROM knowledge.similarity_edges
        WHERE doc_type = %s AND method = %s
    """
    with conn.cursor() as cur:
        cur.execute(query, (graph_config.doc_type, graph_config.method))


def cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    return sum(a * b for a, b in zip(vec_a, vec_b, strict=True))


def normalize_vector(vec: list[float]) -> list[float]:
    norm = math.sqrt(sum(x * x for x in vec))
    if norm == 0:
        return vec
    return [x / norm for x in vec]


def parse_pgvector_text(raw: str) -> list[float]:
    cleaned = raw.strip().strip("[]")
    if not cleaned:
        return []
    return [float(value) for value in cleaned.split(",")]


def pgvector_literal(vector: list[float]) -> str:
    return "[" + ", ".join(f"{value:.8f}" for value in vector) + "]"


def chunked(items: Sequence[PostExtracted], size: int) -> Iterable[Sequence[PostExtracted]]:
    if size <= 0:
        raise ValueError("Размер batch должен быть больше нуля")
    for idx in range(0, len(items), size):
        yield items[idx : idx + size]


def build_dsn() -> str:
    if os.getenv("DATABASE_URL"):
        return os.environ["DATABASE_URL"]
    host = os.getenv("PGHOST", "localhost")
    port = os.getenv("PGPORT", "5432")
    user = os.getenv("PGUSER", "postgres")
    password = os.getenv("PGPASSWORD", "")
    database = os.getenv("PGDATABASE", "postgres")
    return f"dbname={database} user={user} password={password} host={host} port={port}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Построение embeddings и similarity graph для постов")
    parser.add_argument("--source-root", type=Path, required=False)
    parser.add_argument("--config", type=Path, required=False)
    parser.add_argument("--model", type=str, required=False)
    parser.add_argument("--provider", type=str, default=None)
    parser.add_argument("--batch-size", type=int, default=None)
    parser.add_argument("--k", type=int, default=None)
    parser.add_argument("--min-similarity", type=float, default=None)
    parser.add_argument("--limit-posts", type=int, default=None)
    parser.add_argument("--mode", type=str, choices=("incremental", "full"), default=None)
    parser.add_argument("--full-rebuild", action="store_true")
    return parser.parse_args()


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    args = parse_args()
    source_root = args.source_root or (
        Path(__file__).resolve().parents[2]
        / "source_of_truth"
        / "docs"
        / "publications"
        / "blogs"
    )
    config_path = args.config or (Path(__file__).resolve().parents[1] / "config.json")
    pipeline_config = load_config(config_path)

    embedding_config = apply_cli_embeddings(pipeline_config.embeddings, args)
    graph_config = apply_cli_graph(pipeline_config.graph, args)
    execution_config = apply_cli_execution(pipeline_config.execution, args)

    run_pipeline(
        source_root=source_root,
        db_config=DbConfig(dsn=build_dsn()),
        embedding_config=embedding_config,
        graph_config=graph_config,
        execution_config=execution_config,
        full_rebuild=args.full_rebuild,
    )


def load_config(path: Path) -> PipelineConfig:
    data = {}
    if path.exists():
        data = json.loads(path.read_text(encoding="utf-8"))

    embeddings_data = data.get("embeddings") or {}
    graph_data = data.get("graph") or {}
    execution_data = data.get("execution") or {}

    embeddings = EmbeddingConfig(
        provider=str(embeddings_data.get("provider") or os.getenv("EMBEDDINGS_PROVIDER") or "openai"),
        model=str(embeddings_data.get("model") or os.getenv("EMBEDDINGS_MODEL") or "text-embedding-3-large"),
        batch_size=int(embeddings_data.get("batch_size") or os.getenv("EMBEDDINGS_BATCH_SIZE") or 16),
        normalize_text=bool(
            embeddings_data.get("normalize_text")
            if embeddings_data.get("normalize_text") is not None
            else os.getenv("EMBEDDINGS_NORMALIZE_TEXT", "true").lower() == "true"
        ),
    )
    graph = GraphConfig(
        method=str(graph_data.get("method") or os.getenv("GRAPH_METHOD") or "topk"),
        k=int(graph_data.get("top_k") or os.getenv("GRAPH_TOP_K") or 8),
        min_similarity=float(
            graph_data.get("min_similarity") or os.getenv("GRAPH_MIN_SIMILARITY") or 0.75
        ),
    )
    execution = ExecutionConfig(
        mode=str(execution_data.get("mode") or os.getenv("EXECUTION_MODE") or "incremental"),
        limit_posts=(
            int(execution_data.get("limit_posts"))
            if execution_data.get("limit_posts") is not None
            else (int(os.getenv("EXECUTION_LIMIT_POSTS")) if os.getenv("EXECUTION_LIMIT_POSTS") else None)
        ),
    )
    return PipelineConfig(embeddings=embeddings, graph=graph, execution=execution)


def apply_cli_embeddings(config: EmbeddingConfig, args: argparse.Namespace) -> EmbeddingConfig:
    return EmbeddingConfig(
        provider=args.provider or config.provider,
        model=args.model or config.model,
        batch_size=args.batch_size or config.batch_size,
        normalize_text=config.normalize_text,
    )


def apply_cli_graph(config: GraphConfig, args: argparse.Namespace) -> GraphConfig:
    return GraphConfig(
        method=config.method,
        k=args.k or config.k,
        min_similarity=args.min_similarity or config.min_similarity,
    )


def apply_cli_execution(config: ExecutionConfig, args: argparse.Namespace) -> ExecutionConfig:
    return ExecutionConfig(
        mode=args.mode or config.mode,
        limit_posts=args.limit_posts if args.limit_posts is not None else config.limit_posts,
    )


def apply_limit(posts: list[PostExtracted], limit: int | None) -> list[PostExtracted]:
    if limit is None or limit <= 0:
        return posts
    return posts[:limit]


if __name__ == "__main__":
    main()
