"""Простейший mock-клиент, который валидирует контракт ответа /v1/graph как это делал бы фронт."""

import json
import os
import sys
from pathlib import Path


def main() -> None:
    os.environ.setdefault('DATABASE_URL', 'postgresql://test:test@localhost:5432/test')
    api_dir = Path(__file__).resolve().parents[1] / 'api'
    if str(api_dir) not in sys.path:
        sys.path.insert(0, str(api_dir))

    from app.schemas.graph import GraphResponse  # pylint: disable=import-outside-toplevel

    sample_response = {
        'nodes': [
            {
                'id': 'post-1',
                'type': 'publish-post',
                'label': 'post-1',
                'year': 2024,
                'channels': ['site'],
                'rubric_ids': ['core'],
                'category_ids': ['ecosystem'],
                'authors': ['detai'],
                'meta': {},
            }
        ],
        'edges': [
            {
                'source': 'post-1',
                'target': 'post-2',
                'type': 'SIMILAR_UNDIRECTED',
                'weight': 0.92,
                'meta': {},
            }
        ],
        'meta': {
            'filters_applied': {
                'channels': ['site'],
                'years': {'from': 2024, 'to': 2024},
                'authors': [],
                'rubric_ids': ['core'],
                'category_ids': ['ecosystem'],
                'limit_nodes': 200,
            },
            'total_nodes': 1,
            'total_edges': 1,
            'truncated': False,
        },
    }

    parsed = GraphResponse.model_validate(sample_response)
    print(json.dumps(parsed.model_dump(by_alias=True), ensure_ascii=False))


if __name__ == '__main__':
    main()
