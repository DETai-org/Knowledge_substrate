from typing import Literal

from pydantic import BaseModel, Field


class GraphNode(BaseModel):
    id: str
    type: str = 'publish-post'
    label: str
    year: int | None = None
    channels: list[str] = Field(default_factory=list)
    rubric_ids: list[str] = Field(default_factory=list)
    category_ids: list[str] = Field(default_factory=list)
    authors: list[str] = Field(default_factory=list)
    meta: dict = Field(default_factory=dict)


class GraphEdge(BaseModel):
    source: str
    target: str
    type: str = 'SIMILAR_UNDIRECTED'
    weight: float
    meta: dict = Field(default_factory=dict)


class GraphYearsFilter(BaseModel):
    from_: int | None = Field(default=None, alias='from')
    to: int | None = None

    model_config = {'populate_by_name': True}


class GraphFiltersApplied(BaseModel):
    channels: list[str] = Field(default_factory=list)
    years: GraphYearsFilter
    authors: list[str] = Field(default_factory=list)
    rubric_ids: list[str] = Field(default_factory=list)
    category_ids: list[str] = Field(default_factory=list)
    limit_nodes: int
    edge_scope: Literal['local', 'global'] = 'local'


class GraphMeta(BaseModel):
    filters_applied: GraphFiltersApplied
    total_nodes: int
    total_edges: int
    truncated: bool = False


class GraphResponse(BaseModel):
    nodes: list[GraphNode]
    edges: list[GraphEdge]
    meta: GraphMeta
