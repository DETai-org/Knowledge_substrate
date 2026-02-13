import logging
from fastapi import APIRouter, HTTPException, Query

from app.schemas.graph import GraphResponse
from app.services.graph_query import GraphFilters, GraphQueryService

router = APIRouter(prefix='/v1', tags=['graph'])
service = GraphQueryService()
logger = logging.getLogger(__name__)


def _normalize_filter_values(values: list[str] | None, field_name: str) -> list[str] | None:
    if values is None:
        return None

    cleaned = [value.strip() for value in values if value is not None]
    if any(not value for value in cleaned):
        raise HTTPException(status_code=400, detail=f'{field_name} must not contain empty values')
    if not cleaned:
        return None
    return cleaned


@router.get(
    '/graph',
    response_model=GraphResponse,
    responses={
        200: {'description': 'Успешный ответ (включая пустой граф).'},
        400: {'description': 'Некорректный query (например, пустые значения фильтров).'},
        422: {'description': 'Семантически невалидные параметры (например, year_from > year_to).'},
        500: {'description': 'Внутренняя ошибка выполнения запроса.'},
    },
)
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
            channels=_normalize_filter_values(channels, 'channels'),
            year_from=year_from,
            year_to=year_to,
            rubric_ids=_normalize_filter_values(rubric_ids, 'rubric_ids'),
            category_ids=_normalize_filter_values(category_ids, 'category_ids'),
            authors=_normalize_filter_values(authors, 'authors'),
            limit_nodes=limit_nodes,
        )
        response = service.fetch_graph(filters)
        logger.info(
            'event=graph_result nodes_count=%s edges_count=%s truncated=%s',
            response.meta.total_nodes,
            response.meta.total_edges,
            response.meta.truncated,
        )
        return response
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=500, detail='graph query failed') from exc
