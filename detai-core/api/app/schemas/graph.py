from pydantic import BaseModel, Field


class GraphNode(BaseModel):
    id: str
    title: str | None = None
    year: int | None = None
    channels: list[str] = Field(default_factory=list)
    authors: list[str] = Field(default_factory=list)


class GraphEdge(BaseModel):
    source: str
    target: str
    weight: float


class GraphMeta(BaseModel):
    limit_nodes: int
    nodes_count: int
    edges_count: int
    truncated: bool = False


class GraphResponse(BaseModel):
    nodes: list[GraphNode]
    edges: list[GraphEdge]
    meta: GraphMeta
