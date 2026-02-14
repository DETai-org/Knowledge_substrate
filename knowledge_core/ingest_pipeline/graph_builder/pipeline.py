from __future__ import annotations

import argparse
import json
import logging
import math
import os
import re
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence
from urllib import request

import psycopg2
import psycopg2.extras

from knowledge_core.ingest_pipeline.logging import (
    log_error as log_error_event,
    log_event as log_event_message,
)
from knowledge_core.ingest_pipeline.posts import PostExtracted, extract_publish_posts


logger = logging.getLogger(__name__)

OPENAI_KEY_PATTERN = re.compile(r"^sk-[A-Za-z0-9_-]{20,}$")


@dataclass(frozen=True)
class EmbeddingConfig:
    model: str
    batch_size: int
    provider: str
    normalize_text: bool = True
    max_chars: int | None = None


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
    min_posts: int
    dry_run: bool
    fail_fast: bool


@dataclass(frozen=True)
class ExtractConfig:
    prefer_channel: str | None


@dataclass(frozen=True)
class PipelineConfig:
    embeddings: EmbeddingConfig
    graph: GraphConfig
    execution: ExecutionConfig
    extract: ExtractConfig


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
    extract_config: ExtractConfig,
    full_rebuild: bool,
    run_id: str,
    run_embeddings: bool = True,
    run_edges: bool = True,
) -> None:
    full_rebuild = full_rebuild or execution_config.mode == "full"
    posts = extract_publish_posts(source_root, prefer_channel=extract_config.prefer_channel)
    posts = apply_limit(posts, execution_config.limit_posts)
    log_event(run_id, "extract", "publish-посты извлечены", posts=len(posts))

    embeddings: list[EmbeddingRecord] = []
    recalculated_count = 0

    with psycopg2.connect(db_config.dsn) as conn:
        conn.autocommit = False

        if execution_config.dry_run:
            log_event(run_id, "dry_run", "dry-run активен, вычисления и запись пропущены")
            return

        if run_embeddings:
            provider = build_provider(embedding_config)
            normalized_texts = {
                post.id: prepare_text(
                    post.text_for_embedding,
                    normalize=embedding_config.normalize_text,
                    max_chars=embedding_config.max_chars,
                    doc_id=post.id,
                    run_id=run_id,
                )
                for post in posts
            }
            existing = fetch_existing_embeddings(
                conn,
                doc_ids=[post.id for post in posts],
                doc_type=graph_config.doc_type,
                model=embedding_config.model,
            )
            embeddings, reused_count, recalculated_count = build_embeddings(
                provider,
                posts=posts,
                normalized_texts=normalized_texts,
                existing=existing,
                doc_type=graph_config.doc_type,
                model=embedding_config.model,
                conn=conn,
                fail_fast=execution_config.fail_fast,
                run_id=run_id,
            )
            log_event(
                run_id,
                "embed",
                "embeddings рассчитаны",
                reused=reused_count,
                recalculated=recalculated_count,
                model=embedding_config.model,
                batch=embedding_config.batch_size,
                docs_count=len(embeddings),
            )

        if run_edges:
            if not embeddings:
                embeddings = fetch_embeddings_for_edges(
                    conn,
                    doc_type=graph_config.doc_type,
                    model=embedding_config.model,
                )
            if full_rebuild:
                clear_edges(conn, graph_config)

            edges = build_similarity_edges(embeddings, graph_config)
            log_event(
                run_id,
                "knn",
                "edges подготовлены",
                edges=len(edges),
                top_k=graph_config.k,
                min_similarity=graph_config.min_similarity,
            )
            edges_written = persist_edges(
                conn,
                edges,
                graph_config=graph_config,
                affected_doc_ids={record.doc_id for record in embeddings},
                full_rebuild=full_rebuild,
            )
            log_event(
                run_id,
                "persist",
                "запись завершена",
                embeddings_upserted=recalculated_count,
                edges_upserted=edges_written,
            )

        conn.commit()


def build_provider(config: EmbeddingConfig) -> EmbeddingProvider:
    provider = config.provider.lower()
    if provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY", "")
        return OpenAIEmbeddingProvider(config.model, config.batch_size, api_key)
    raise ValueError(f"Неизвестный провайдер embeddings: {config.provider}")


def validate_openai_key_format(api_key: str) -> None:
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY не задан")
    if not OPENAI_KEY_PATTERN.match(api_key):
        raise RuntimeError("OPENAI_API_KEY не похож на валидный ключ")


def validate_openai_embeddings_access(
    api_key: str,
    model: str,
    batch_size: int,
    run_id: str,
) -> None:
    provider = OpenAIEmbeddingProvider(model=model, batch_size=batch_size, api_key=api_key)
    try:
        provider.embed_texts(["ping"])
    except Exception as exc:
        log_error(run_id, "preflight", exc)
        raise RuntimeError("Не удалось подтвердить доступ к embeddings OpenAI") from exc


def normalize_text(text: str) -> str:
    lowered = text.lower()
    normalized = re.sub(r"\s+", " ", lowered).strip()
    return normalized


def prepare_text(
    text: str,
    normalize: bool,
    max_chars: int | None,
    doc_id: str,
    run_id: str,
) -> str:
    prepared = normalize_text(text) if normalize else text
    if max_chars is not None and max_chars > 0 and len(prepared) > max_chars:
        log_event(
            run_id,
            "extract",
            "текст обрезан по лимиту символов",
            doc_id=doc_id,
            max_chars=max_chars,
        )
        return prepared[:max_chars]
    return prepared


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


def fetch_embeddings_for_edges(
    conn: psycopg2.extensions.connection,
    doc_type: str,
    model: str,
) -> list[EmbeddingRecord]:
    query = """
        SELECT doc_id::text, source_hash, embedding::text
        FROM knowledge.embeddings
        WHERE doc_type = %s AND model = %s
    """
    with conn.cursor() as cur:
        cur.execute(query, (doc_type, model))
        rows = cur.fetchall()
    return [
        EmbeddingRecord(
            doc_id=str(doc_id),
            source_hash=source_hash,
            vector=parse_pgvector_text(embedding_text),
        )
        for doc_id, source_hash, embedding_text in rows
    ]


def build_embeddings(
    provider: EmbeddingProvider,
    posts: list[PostExtracted],
    normalized_texts: dict[str, str],
    existing: dict[str, EmbeddingRecord],
    doc_type: str,
    model: str,
    conn: psycopg2.extensions.connection,
    fail_fast: bool,
    run_id: str,
) -> tuple[list[EmbeddingRecord], int, int]:
    to_update: list[PostExtracted] = []
    embeddings: list[EmbeddingRecord] = []
    reused_count = 0
    recalculated_count = 0

    for post in posts:
        record = existing.get(post.id)
        if record and record.source_hash == post.source_hash:
            embeddings.append(record)
            reused_count += 1
            continue
        to_update.append(post)

    recalculated_count += process_batches(
        provider,
        to_update,
        normalized_texts,
        embeddings,
        conn,
        doc_type,
        model,
        fail_fast=fail_fast,
        run_id=run_id,
    )

    return embeddings, reused_count, recalculated_count


def process_batches(
    provider: EmbeddingProvider,
    posts: list[PostExtracted],
    normalized_texts: dict[str, str],
    embeddings: list[EmbeddingRecord],
    conn: psycopg2.extensions.connection,
    doc_type: str,
    model: str,
    fail_fast: bool,
    run_id: str,
) -> int:
    recalculated_count = 0
    batch_size = provider.batch_size
    start = 0
    while start < len(posts):
        current_size = min(batch_size, len(posts) - start)
        batch = posts[start : start + current_size]
        try:
            vectors = embed_with_retry(
                provider,
                [normalized_texts[item.id] for item in batch],
                run_id=run_id,
                doc_ids=[item.id for item in batch],
                fail_fast=fail_fast,
            )
        except Exception as exc:
            log_error(
                run_id,
                "embed",
                exc,
                doc_ids=[item.id for item in batch],
            )
            if fail_fast:
                raise
            if current_size <= 1:
                raise
            logger.warning("⚠️ Падение batch=%s, уменьшаем размер: %s", current_size, exc)
            batch_size = max(1, current_size // 2)
            continue

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
        recalculated_count += len(updated_records)

        upsert_embeddings(
            conn,
            updated_records,
            doc_type=doc_type,
            model=model,
        )
        start += current_size

    return recalculated_count


def embed_with_retry(
    provider: EmbeddingProvider,
    texts: Sequence[str],
    run_id: str,
    doc_ids: list[str],
    fail_fast: bool,
) -> list[list[float]]:
    delays = (1, 2, 4)
    for attempt, delay in enumerate(delays, start=1):
        try:
            return provider.embed_texts(texts)
        except Exception as exc:
            if attempt == len(delays):
                raise
            log_error(
                run_id,
                "embed",
                exc,
                doc_ids=doc_ids,
                attempt=attempt,
            )
            if fail_fast:
                raise
            time_sleep(delay)
    raise RuntimeError("Не удалось получить embeddings после повторов")


def time_sleep(seconds: int) -> None:
    import time

    time.sleep(seconds)


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
) -> int:
    if not full_rebuild and affected_doc_ids:
        delete_edges_for_docs(conn, graph_config, affected_doc_ids)

    if not edges:
        return 0

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
          (source_id, target_id, doc_type, weight, method, k, min_similarity)
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
    return len(values)


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
    parser.add_argument("--max-chars", type=int, default=None)
    parser.add_argument("--k", type=int, default=None)
    parser.add_argument("--min-similarity", type=float, default=None)
    parser.add_argument("--limit-posts", type=int, default=None)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--mode", type=str, choices=("incremental", "full"), default=None)
    parser.add_argument("--min-posts", type=int, default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--fail-fast", action="store_true")
    parser.add_argument("--full", action="store_true")
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
    config_path = args.config or Path(
        os.getenv("CONFIG_PATH", Path(__file__).resolve().parents[1] / "config.json")
    )
    if not config_path.exists():
        raise FileNotFoundError(f"config.json не найден: {config_path}")
    pipeline_config = load_config(config_path)

    embedding_config = apply_cli_embeddings(pipeline_config.embeddings, args)
    graph_config = apply_cli_graph(pipeline_config.graph, args)
    execution_config = apply_cli_execution(pipeline_config.execution, args)
    extract_config = pipeline_config.extract

    run_id = uuid.uuid4().hex[:8]
    log_event(
        run_id,
        "start",
        "запуск пайплайна",
        model=embedding_config.model,
        top_k=graph_config.k,
        min_similarity=graph_config.min_similarity,
        mode=execution_config.mode,
        prefer_channel=extract_config.prefer_channel,
    )

    preflight(
        run_id=run_id,
        config_path=config_path,
        db_config=DbConfig(dsn=build_dsn()),
        embedding_config=embedding_config,
        graph_config=graph_config,
        execution_config=execution_config,
        extract_config=extract_config,
        source_root=source_root,
    )

    run_pipeline(
        source_root=source_root,
        db_config=DbConfig(dsn=build_dsn()),
        embedding_config=embedding_config,
        graph_config=graph_config,
        execution_config=execution_config,
        extract_config=extract_config,
        full_rebuild=args.full_rebuild or args.full,
        run_id=run_id,
    )


def load_config(path: Path) -> PipelineConfig:
    data = {}
    if path.exists():
        data = json.loads(path.read_text(encoding="utf-8"))

    embeddings_data = data.get("embeddings") or {}
    graph_data = data.get("graph") or {}
    execution_data = data.get("execution") or {}
    extract_data = data.get("extract") or {}

    embeddings = EmbeddingConfig(
        provider=str(embeddings_data.get("provider") or os.getenv("EMBEDDINGS_PROVIDER") or "openai"),
        model=str(embeddings_data.get("model") or os.getenv("EMBEDDINGS_MODEL") or "text-embedding-3-large"),
        batch_size=int(embeddings_data.get("batch_size") or os.getenv("EMBEDDINGS_BATCH_SIZE") or 32),
        normalize_text=bool(
            embeddings_data.get("normalize_text")
            if embeddings_data.get("normalize_text") is not None
            else os.getenv("EMBEDDINGS_NORMALIZE_TEXT", "true").lower() == "true"
        ),
        max_chars=(
            int(embeddings_data.get("max_chars"))
            if embeddings_data.get("max_chars") is not None
            else (int(os.getenv("EMBEDDINGS_MAX_CHARS")) if os.getenv("EMBEDDINGS_MAX_CHARS") else None)
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
        min_posts=int(
            execution_data.get("min_posts")
            if execution_data.get("min_posts") is not None
            else os.getenv("EXECUTION_MIN_POSTS") or 1
        ),
        dry_run=bool(
            execution_data.get("dry_run")
            if execution_data.get("dry_run") is not None
            else os.getenv("EXECUTION_DRY_RUN", "false").lower() == "true"
        ),
        fail_fast=bool(
            execution_data.get("fail_fast")
            if execution_data.get("fail_fast") is not None
            else os.getenv("EXECUTION_FAIL_FAST", "false").lower() == "true"
        ),
    )
    extract = ExtractConfig(
        prefer_channel=(
            str(extract_data.get("prefer_channel"))
            if extract_data.get("prefer_channel") is not None
            else os.getenv("EXTRACT_PREFER_CHANNEL")
        )
    )
    return PipelineConfig(
        embeddings=embeddings,
        graph=graph,
        execution=execution,
        extract=extract,
    )


def apply_cli_embeddings(config: EmbeddingConfig, args: argparse.Namespace) -> EmbeddingConfig:
    return EmbeddingConfig(
        provider=args.provider or config.provider,
        model=args.model or config.model,
        batch_size=args.batch_size or config.batch_size,
        normalize_text=config.normalize_text,
        max_chars=args.max_chars if args.max_chars is not None else config.max_chars,
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
        limit_posts=(
            args.limit
            if args.limit is not None
            else (args.limit_posts if args.limit_posts is not None else config.limit_posts)
        ),
        min_posts=args.min_posts if args.min_posts is not None else config.min_posts,
        dry_run=args.dry_run or config.dry_run,
        fail_fast=args.fail_fast or config.fail_fast,
    )


def apply_limit(posts: list[PostExtracted], limit: int | None) -> list[PostExtracted]:
    if limit is None or limit <= 0:
        return posts
    return posts[:limit]


def preflight(
    run_id: str,
    config_path: Path,
    db_config: DbConfig,
    embedding_config: EmbeddingConfig,
    graph_config: GraphConfig,
    execution_config: ExecutionConfig,
    extract_config: ExtractConfig,
    source_root: Path,
) -> None:
    try:
        if not config_path.exists():
            raise RuntimeError("config.json не найден")

        if embedding_config.provider.lower() == "openai":
            api_key = os.getenv("OPENAI_API_KEY", "")
            if api_key:
                validate_openai_key_format(api_key)
            elif not execution_config.dry_run:
                raise RuntimeError(
                    "OPENAI_API_KEY не задан для режима non-dry-run и провайдера openai"
                )

        json.loads(config_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        error = RuntimeError(f"config.json не читается: {exc}")
        log_error(run_id, "preflight", error)
        raise error from exc
    except Exception as exc:
        log_error(run_id, "preflight", exc)
        raise

    try:
        if (
            not execution_config.dry_run
            and embedding_config.provider.lower() == "openai"
        ):
            api_key = os.getenv("OPENAI_API_KEY", "")
            validate_openai_key_format(api_key)
            validate_openai_embeddings_access(
                api_key=api_key,
                model=embedding_config.model,
                batch_size=embedding_config.batch_size,
                run_id=run_id,
            )

        posts = extract_publish_posts(source_root, prefer_channel=extract_config.prefer_channel)
        posts = apply_limit(posts, execution_config.limit_posts)
        if len(posts) < execution_config.min_posts:
            raise RuntimeError(
                f"Найдено publish-постов меньше минимума: {len(posts)} < {execution_config.min_posts}"
            )

        with psycopg2.connect(db_config.dsn) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
                cur.execute(
                    """
                    SELECT to_regclass('knowledge.embeddings'),
                           to_regclass('knowledge.similarity_edges')
                    """
                )
                embeddings_table, edges_table = cur.fetchone()
                if embeddings_table is None or edges_table is None:
                    raise RuntimeError("Не найдены таблицы embeddings/similarity_edges")
    except psycopg2.OperationalError as exc:
        error = RuntimeError(
            "Не удалось подключиться к Postgres: проверьте параметры подключения"
        )
        log_error(run_id, "preflight", error)
        raise error from exc
    except Exception as exc:
        log_error(run_id, "preflight", exc)
        raise

    log_event(
        run_id,
        "preflight",
        "preflight пройден",
        model=embedding_config.model,
        top_k=graph_config.k,
        min_similarity=graph_config.min_similarity,
        mode=execution_config.mode,
        posts=len(posts),
    )


def log_event(run_id: str, stage: str, message: str, **fields: object) -> None:
    log_event_message(logger, run_id, stage, message, **fields)


def log_error(
    run_id: str,
    stage: str,
    exc: Exception,
    doc_id: str | None = None,
    source_path: str | None = None,
    doc_ids: list[str] | None = None,
    attempt: int | None = None,
) -> None:
    log_error_event(
        logger,
        run_id,
        stage,
        str(exc),
        error=type(exc).__name__,
        doc_id=doc_id,
        source_path=source_path,
        doc_ids=','.join((doc_ids or [])[:5]) if doc_ids else None,
        attempt=attempt,
    )


if __name__ == "__main__":
    main()
