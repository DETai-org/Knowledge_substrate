from fastapi import APIRouter, HTTPException

from app.services.document_service import DocumentService

router = APIRouter(tags=['health'])
service = DocumentService()


@router.get('/health')
def health() -> dict:
    return {'status': 'ok', 'service': 'detai-core-api'}


@router.get('/db/health')
def db_health() -> dict:
    try:
        service.db_health()
        return {'db': 'ok'}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f'db error: {exc!s}') from exc
