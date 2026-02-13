from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.document_service import ALLOWED_ZONES, DocInput, DocumentService

router = APIRouter(tags=['documents'])
service = DocumentService()


class DocIn(BaseModel):
    zone: str = 'private'
    source: Optional[str] = None
    title: Optional[str] = None
    content: str
    meta: dict = {}


@router.post('/docs')
def create_doc(doc: DocIn) -> dict:
    if doc.zone not in ALLOWED_ZONES:
        raise HTTPException(status_code=400, detail='zone must be public|team|private')
    try:
        new_id = service.create_doc(
            DocInput(
                zone=doc.zone,
                source=doc.source,
                title=doc.title,
                content=doc.content,
                meta=doc.meta,
            )
        )
        return {'id': new_id}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f'insert failed: {exc!s}') from exc


@router.get('/docs/{doc_id}')
def get_doc(doc_id: int) -> dict:
    document = service.get_doc(doc_id)
    if not document:
        raise HTTPException(status_code=404, detail='not found')
    return document


@router.get('/search')
def search(q: str, zone: Optional[str] = None, limit: int = 10) -> list[dict]:
    if limit < 1 or limit > 50:
        raise HTTPException(status_code=400, detail='limit must be 1..50')
    if zone and zone not in ALLOWED_ZONES:
        raise HTTPException(status_code=400, detail='zone must be public|team|private')
    return service.search(query_text=q, zone=zone, limit=limit)
