from fastapi import APIRouter, HTTPException, Query

from app.schemas.graph import GraphResponse
from app.services.graph_query import GraphFilters, GraphQueryService

router = APIRouter(prefix='/v1', tags=['graph'])
service = GraphQueryService()


@router.get('/graph', response_model=GraphResponse)
def get_graph(
    channels: list[str] | None = Query(default=None),
    year_from: int | None = Query(default=None, ge=1900, le=2100),
    year_to: int | None = Query(default=None, ge=1900, le=2100),
    rubric_ids: list[str] | None = Query(default=None),
    category_ids: list[str] | None = Query(default=None),
    authors: list[str] | None = Query(default=None),
    limit_nodes: int = Query(default=200, ge=1, le=1000),
) -> GraphResponse:

    if year_from is not None and year_to is not None and year_from > year_to:
        raise HTTPException(status_code=422, detail='year_from must be less or equal year_to')

    try:
        filters = GraphFilters(
            channels=channels,
            year_from=year_from,
            year_to=year_to,
            rubric_ids=rubric_ids,
            category_ids=category_ids,
            authors=authors,
            limit_nodes=limit_nodes,
        )
        return service.fetch_graph(filters)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f'graph query failed: {exc!s}') from exc
