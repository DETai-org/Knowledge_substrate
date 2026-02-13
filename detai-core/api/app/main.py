from fastapi import FastAPI

from app.core.config import get_settings
from app.core.logging import configure_logging
from app.routers.docs import router as docs_router
from app.routers.graph import router as graph_router
from app.routers.health import router as health_router

settings = get_settings()
configure_logging()

app = FastAPI(title=settings.api_title, version=settings.api_version)
app.include_router(health_router)
app.include_router(docs_router)
app.include_router(graph_router)
