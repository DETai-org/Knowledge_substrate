from __future__ import annotations

from dataclasses import dataclass

import psycopg

from app.core.config import get_settings

ALLOWED_ZONES = ('public', 'team', 'private')


@dataclass
class DocInput:
    zone: str
    source: str | None
    title: str | None
    content: str
    meta: dict


class DocumentService:
    def __init__(self) -> None:
        self._settings = get_settings()

    def _connect(self):
        return psycopg.connect(self._settings.database_url)

    def create_doc(self, payload: DocInput) -> int:
        query = """
        INSERT INTO knowledge.documents (zone, source, title, content, meta)
        VALUES (%s, %s, %s, %s, %s::jsonb)
        RETURNING id;
        """
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    query,
                    (
                        payload.zone,
                        payload.source,
                        payload.title,
                        payload.content,
                        psycopg.types.json.Json(payload.meta),
                    ),
                )
                new_id = cur.fetchone()[0]
                conn.commit()
                return int(new_id)

    def get_doc(self, doc_id: int) -> dict | None:
        query = """
        SELECT id, zone, source, title, content, meta, created_at, updated_at
        FROM knowledge.documents
        WHERE id = %s;
        """
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (doc_id,))
                row = cur.fetchone()
                if not row:
                    return None
                keys = ['id', 'zone', 'source', 'title', 'content', 'meta', 'created_at', 'updated_at']
                return dict(zip(keys, row))

    def search(self, query_text: str, zone: str | None, limit: int) -> list[dict]:
        if zone:
            sql = """
            SELECT id, zone, title
            FROM knowledge.documents
            WHERE zone = %s
              AND fts @@ plainto_tsquery('simple', %s)
            ORDER BY ts_rank(fts, plainto_tsquery('simple', %s)) DESC
            LIMIT %s;
            """
            params = (zone, query_text, query_text, limit)
        else:
            sql = """
            SELECT id, zone, title
            FROM knowledge.documents
            WHERE fts @@ plainto_tsquery('simple', %s)
            ORDER BY ts_rank(fts, plainto_tsquery('simple', %s)) DESC
            LIMIT %s;
            """
            params = (query_text, query_text, limit)

        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                rows = cur.fetchall()
                return [{'id': r[0], 'zone': r[1], 'title': r[2]} for r in rows]

    def db_health(self) -> None:
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT 1;')
