from __future__ import annotations

import argparse
import csv
import json
import math
import os
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import psycopg2
import psycopg2.extras

from knowledge_core.ingest_pipeline.graph_builder.pipeline import apply_cli_graph, build_dsn, load_config


@dataclass(frozen=True)
class Document:
    doc_id: str
    rubric_ids: list[str]
    channels: list[str]
    date_ymd: str | None
    title: str | None
    seo_lead: str | None
    keywords_raw: Any


@dataclass(frozen=True)
class Edge:
    source_id: str
    target_id: str
    weight: float
    method: str
    k: int
    min_similarity: float
    doc_type: str | None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Экспорт агрегатов для синтеза постулатов')
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--config', type=Path, required=False)
    parser.add_argument('--k', type=int, default=None)
    parser.add_argument('--min-similarity', type=float, default=None)
    parser.add_argument('--model', type=str, default=None)
    parser.add_argument('--core-n', type=int, default=5)
    parser.add_argument('--bridge-n', type=int, default=5)
    parser.add_argument('--edge-n', type=int, default=5)
    return parser.parse_args()


def normalize_rubric_id(rubric_id: str) -> str:
    return rubric_id if rubric_id.startswith('rubric:') else f'rubric:{rubric_id}'


def load_documents(conn: psycopg2.extensions.connection, *, model: str) -> dict[str, Document]:
    query = """
        SELECT
            dm.doc_id::text,
            COALESCE(dm.rubric_ids, ARRAY[]::text[]) AS rubric_ids,
            COALESCE(dm.channels, ARRAY[]::text[]) AS channels,
            dm.date_ymd::text,
            COALESCE(dm.meta->>'title', NULL) AS title,
            COALESCE(dm.meta->>'seoLead', dm.meta->>'seo_lead', NULL) AS seo_lead,
            COALESCE(dm.meta->'keywords_raw', dm.meta->'keywordsRaw', NULL) AS keywords_raw
        FROM knowledge.doc_metadata dm
        WHERE dm.doc_type = 'post'
          AND EXISTS (
              SELECT 1
              FROM knowledge.embeddings e
              WHERE e.doc_id = dm.doc_id
                AND e.doc_type = 'post'
                AND e.model = %s
          )
    """

    docs: dict[str, Document] = {}
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute(query, (model,))
        for row in cur.fetchall():
            docs[row['doc_id']] = Document(
                doc_id=row['doc_id'],
                rubric_ids=[str(x) for x in (row['rubric_ids'] or [])],
                channels=[str(x) for x in (row['channels'] or [])],
                date_ymd=row['date_ymd'],
                title=row['title'],
                seo_lead=row['seo_lead'],
                keywords_raw=row['keywords_raw'],
            )
    return docs


def load_edges(
    conn: psycopg2.extensions.connection,
    *,
    model: str,
    method: str,
    k: int,
    min_similarity: float,
) -> list[Edge]:
    query = """
        SELECT se.source_id::text, se.target_id::text, se.weight, se.method, se.k, se.min_similarity, se.doc_type
        FROM knowledge.similarity_edges se
        WHERE se.doc_type = 'post'
          AND se.method = %s
          AND se.k = %s
          AND se.min_similarity = %s
          AND EXISTS (
              SELECT 1
              FROM knowledge.embeddings es
              WHERE es.doc_id = se.source_id
                AND es.doc_type = 'post'
                AND es.model = %s
          )
          AND EXISTS (
              SELECT 1
              FROM knowledge.embeddings et
              WHERE et.doc_id = se.target_id
                AND et.doc_type = 'post'
                AND et.model = %s
          )
    """
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute(query, (method, k, min_similarity, model, model))
        rows = cur.fetchall()

    if not rows:
        raise RuntimeError('similarity_edges empty; run ingest stages embeddings+edges first')

    return [
        Edge(
            source_id=row['source_id'],
            target_id=row['target_id'],
            weight=float(row['weight']),
            method=row['method'],
            k=int(row['k']),
            min_similarity=float(row['min_similarity']),
            doc_type=row.get('doc_type'),
        )
        for row in rows
    ]


def write_counts_by_rubric(out_dir: Path, documents: dict[str, Document]) -> dict[str, int]:
    counter: Counter[str] = Counter()
    for doc in documents.values():
        for rubric_id in set(doc.rubric_ids):
            counter[rubric_id] += 1

    aggregates_dir = out_dir / 'aggregates'
    aggregates_dir.mkdir(parents=True, exist_ok=True)
    path = aggregates_dir / 'counts_by_rubric.csv'
    with path.open('w', encoding='utf-8', newline='') as fh:
        writer = csv.writer(fh)
        writer.writerow(['rubric_id', 'count_posts'])
        for rubric_id, count in sorted(counter.items(), key=lambda item: (-item[1], item[0])):
            writer.writerow([rubric_id, count])
    return dict(counter)


def percentile_25(values: list[float]) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    idx = max(0, math.ceil(0.25 * len(ordered)) - 1)
    return ordered[idx]


def aggregate_bridge_targets(links: list[dict[str, Any]], rubric_id: str) -> tuple[dict[str, float], dict[str, list[dict[str, Any]]]]:
    by_rubric_weight: dict[str, float] = defaultdict(float)
    top_links: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for link in links:
        target_doc_rubrics: list[str] = link['target_rubrics']
        target_candidates = [rid for rid in target_doc_rubrics if rid != rubric_id]
        if not target_candidates:
            continue

        share_piece = link['weight'] / len(target_candidates)
        for target_rubric in target_candidates:
            by_rubric_weight[target_rubric] += share_piece
            top_links[target_rubric].append({'target_doc_id': link['target_doc_id'], 'weight': link['weight']})

    for target_rubric, items in top_links.items():
        uniq: dict[str, dict[str, Any]] = {}
        for item in items:
            prev = uniq.get(item['target_doc_id'])
            if prev is None or item['weight'] > prev['weight']:
                uniq[item['target_doc_id']] = item
        top_links[target_rubric] = sorted(uniq.values(), key=lambda item: item['weight'], reverse=True)[:5]

    return by_rubric_weight, top_links


def build_selection(
    documents: dict[str, Document],
    edges: list[Edge],
    rubric_counts: dict[str, int],
    *,
    core_n: int,
    bridge_n: int,
    edge_n: int,
    model: str,
    method: str,
    k: int,
    min_similarity: float,
) -> dict[str, Any]:
    adjacency: dict[str, list[tuple[str, float]]] = defaultdict(list)
    for edge in edges:
        adjacency[edge.source_id].append((edge.target_id, edge.weight))
        adjacency[edge.target_id].append((edge.source_id, edge.weight))

    rubric_to_docs: dict[str, list[str]] = defaultdict(list)
    for doc in documents.values():
        for rubric_id in set(doc.rubric_ids):
            rubric_to_docs[rubric_id].append(doc.doc_id)

    rubrics_output: dict[str, Any] = {}
    for rubric_id in sorted(rubric_to_docs.keys()):
        metrics: list[dict[str, Any]] = []
        for doc_id in rubric_to_docs[rubric_id]:
            intra_weight_sum = 0.0
            intra_degree = 0
            cross_weight_sum = 0.0
            bridge_links: list[dict[str, Any]] = []

            for neighbor_id, weight in adjacency.get(doc_id, []):
                neighbor = documents.get(neighbor_id)
                if not neighbor:
                    continue
                neighbor_rubrics = set(neighbor.rubric_ids)
                if rubric_id in neighbor_rubrics:
                    intra_weight_sum += weight
                    intra_degree += 1
                elif neighbor_rubrics:
                    cross_weight_sum += weight
                    bridge_links.append(
                        {
                            'target_doc_id': neighbor_id,
                            'weight': weight,
                            'target_rubrics': list(neighbor_rubrics),
                        }
                    )

            total_weight_sum = intra_weight_sum + cross_weight_sum
            bridge_ratio = (cross_weight_sum / total_weight_sum) if total_weight_sum > 0 else 0.0
            bridge_weights, top_links = aggregate_bridge_targets(bridge_links, rubric_id)

            metrics.append(
                {
                    'doc_id': doc_id,
                    'intra_weight_sum': intra_weight_sum,
                    'intra_degree': intra_degree,
                    'cross_weight_sum': cross_weight_sum,
                    'total_weight_sum': total_weight_sum,
                    'bridge_ratio': bridge_ratio,
                    'bridge_weights': bridge_weights,
                    'top_links': top_links,
                }
            )

        def with_doc_fields(metric: dict[str, Any], role: str) -> dict[str, Any]:
            doc = documents[metric['doc_id']]
            item = {
                'doc_id': doc.doc_id,
                'title': doc.title,
                'seoLead': doc.seo_lead,
                'keywords_raw': doc.keywords_raw,
                'rubric_ids': doc.rubric_ids,
                'channels': doc.channels,
                'date_ymd': doc.date_ymd,
                'role': role,
                'evidence': {
                    'intra_weight_sum': round(metric['intra_weight_sum'], 6),
                    'intra_degree': metric['intra_degree'],
                    'cross_weight_sum': round(metric['cross_weight_sum'], 6),
                    'total_weight_sum': round(metric['total_weight_sum'], 6),
                    'bridge_ratio': round(metric['bridge_ratio'], 6),
                },
            }
            if role == 'bridge':
                bridge_total = sum(metric['bridge_weights'].values())
                bridge_to = []
                for target_rubric, value in sorted(metric['bridge_weights'].items(), key=lambda x: x[1], reverse=True):
                    share = (value / bridge_total) if bridge_total > 0 else 0.0
                    bridge_to.append({'to_rubric_id': normalize_rubric_id(target_rubric), 'share': round(share, 6)})

                top_links = []
                for target_rubric, items in metric['top_links'].items():
                    top_links.append(
                        {
                            'to_rubric_id': normalize_rubric_id(target_rubric),
                            'links': [
                                {
                                    'target_doc_id': entry['target_doc_id'],
                                    'weight': round(entry['weight'], 6),
                                }
                                for entry in items
                            ],
                        }
                    )
                item['bridge_to'] = bridge_to
                item['top_links'] = sorted(top_links, key=lambda x: x['to_rubric_id'])
            return item

        core = sorted(metrics, key=lambda m: (-m['intra_weight_sum'], -m['intra_degree']))[:core_n]
        bridges = sorted(metrics, key=lambda m: (-m['bridge_ratio'], -m['cross_weight_sum']))[:bridge_n]

        core_ids = {m['doc_id'] for m in core}
        bridge_ids = {m['doc_id'] for m in bridges}

        threshold = percentile_25([m['intra_weight_sum'] for m in metrics])
        edges_candidates = [
            m for m in metrics if m['doc_id'] not in core_ids and m['doc_id'] not in bridge_ids and m['intra_weight_sum'] <= threshold
        ]
        edge_docs = sorted(edges_candidates, key=lambda m: (m['intra_weight_sum'], m['intra_degree']))[:edge_n]

        bridge_totals: dict[str, float] = defaultdict(float)
        for bridge_metric in bridges:
            for target_rubric, value in bridge_metric['bridge_weights'].items():
                bridge_totals[target_rubric] += value
        grand_total = sum(bridge_totals.values())
        bridge_summary = [
            {
                'to_rubric_id': normalize_rubric_id(target_rubric),
                'share': round((value / grand_total) if grand_total > 0 else 0.0, 6),
            }
            for target_rubric, value in sorted(bridge_totals.items(), key=lambda x: x[1], reverse=True)
        ]

        rubrics_output[normalize_rubric_id(rubric_id)] = {
            'counts': {'posts': rubric_counts.get(rubric_id, 0)},
            'core': [with_doc_fields(item, 'core') for item in core],
            'bridges': [with_doc_fields(item, 'bridge') for item in bridges],
            'edges': [with_doc_fields(item, 'edge') for item in edge_docs],
            'bridge_summary': bridge_summary,
        }

    return {
        'meta': {
            'generated_at': datetime.now(tz=UTC).isoformat(),
            'model': model,
            'k': k,
            'min_similarity': min_similarity,
            'method': method,
            'index_field': 'seoLead',
            'note': 'seoLead is an index, not a source of truth; full text must be read for core and bridges',
        },
        'rubrics': rubrics_output,
    }


def main() -> None:
    args = parse_args()
    config_path = args.config or Path(os.getenv('CONFIG_PATH', Path(__file__).resolve().parent / 'config.json'))
    config = load_config(config_path)
    graph_config = apply_cli_graph(config.graph, args)
    model = args.model or config.embeddings.model

    with psycopg2.connect(build_dsn()) as conn:
        documents = load_documents(conn, model=model)
        edges = load_edges(
            conn,
            model=model,
            method=graph_config.method,
            k=graph_config.k,
            min_similarity=graph_config.min_similarity,
        )

    rubric_counts = write_counts_by_rubric(args.out, documents)
    selection = build_selection(
        documents,
        edges,
        rubric_counts,
        core_n=args.core_n,
        bridge_n=args.bridge_n,
        edge_n=args.edge_n,
        model=model,
        method=graph_config.method,
        k=graph_config.k,
        min_similarity=graph_config.min_similarity,
    )

    aggregates_dir = args.out / 'aggregates'
    aggregates_dir.mkdir(parents=True, exist_ok=True)
    snapshot_path = aggregates_dir / 'selection_for_synthesis.json'
    snapshot_path.write_text(json.dumps(selection, ensure_ascii=False, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
