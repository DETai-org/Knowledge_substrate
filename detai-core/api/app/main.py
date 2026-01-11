import os
from typing import Optional

import psycopg
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="DETai Core API", version="0.2.0")

def get_db_url() -> str:
    url = os.getenv("DATABASE_URL")
    if url:
        return url

    env_path = "/srv/detai-core/.env"
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            if k.strip() == "DATABASE_URL":
                return v.strip()

    raise RuntimeError("DATABASE_URL not found")

def db_connect():
    return psycopg.connect(get_db_url())

@app.get("/health")
def health():
    return {"status": "ok", "service": "detai-core-api"}

@app.get("/db/health")
def db_health():
    try:
        with db_connect() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1;")
                return {"db": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"db error: {e!s}")

class DocIn(BaseModel):
    zone: str = "private"
    source: Optional[str] = None
    title: Optional[str] = None
    content: str
    meta: dict = {}

@app.post("/docs")
def create_doc(doc: DocIn):
    if doc.zone not in ("public", "team", "private"):
        raise HTTPException(status_code=400, detail="zone must be public|team|private")

    q = """
    INSERT INTO knowledge.documents (zone, source, title, content, meta)
    VALUES (%s, %s, %s, %s, %s::jsonb)
    RETURNING id;
    """
    try:
        with db_connect() as conn:
            with conn.cursor() as cur:
                cur.execute(q, (doc.zone, doc.source, doc.title, doc.content, psycopg.types.json.Json(doc.meta)))
                new_id = cur.fetchone()[0]
                conn.commit()
        return {"id": new_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"insert failed: {e!s}")

@app.get("/docs/{doc_id}")
def get_doc(doc_id: int):
    q = """
    SELECT id, zone, source, title, content, meta, created_at, updated_at
    FROM knowledge.documents
    WHERE id = %s;
    """
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute(q, (doc_id,))
            row = cur.fetchone()
            if not row:
                raise HTTPException(status_code=404, detail="not found")
            keys = ["id","zone","source","title","content","meta","created_at","updated_at"]
            return dict(zip(keys, row))

@app.get("/search")
def search(q: str, zone: Optional[str] = None, limit: int = 10):
    if limit < 1 or limit > 50:
        raise HTTPException(status_code=400, detail="limit must be 1..50")

    if zone and zone not in ("public", "team", "private"):
        raise HTTPException(status_code=400, detail="zone must be public|team|private")

    if zone:
        sql = """
        SELECT id, zone, title
        FROM knowledge.documents
        WHERE zone = %s
          AND fts @@ plainto_tsquery('simple', %s)
        ORDER BY ts_rank(fts, plainto_tsquery('simple', %s)) DESC
        LIMIT %s;
        """
        params = (zone, q, q, limit)
    else:
        sql = """
        SELECT id, zone, title
        FROM knowledge.documents
        WHERE fts @@ plainto_tsquery('simple', %s)
        ORDER BY ts_rank(fts, plainto_tsquery('simple', %s)) DESC
        LIMIT %s;
        """
        params = (q, q, limit)

    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            rows = cur.fetchall()
            return [{"id": r[0], "zone": r[1], "title": r[2]} for r in rows]
