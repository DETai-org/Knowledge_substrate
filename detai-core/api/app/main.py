import logging
import time
import uuid

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.config import get_settings
from app.core.logging import configure_logging
from app.routers.docs import router as docs_router
from app.routers.graph import router as graph_router
from app.routers.health import router as health_router

settings = get_settings()
configure_logging()
logger = logging.getLogger('api')

app = FastAPI(title=settings.api_title, version=settings.api_version)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=False,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.middleware('http')
async def request_logging_middleware(request: Request, call_next):
    request_id = request.headers.get('x-request-id') or uuid.uuid4().hex[:12]
    start = time.perf_counter()
    request.state.request_id = request_id

    response = await call_next(request)

    duration_ms = int((time.perf_counter() - start) * 1000)
    logger.info(
        'event=request_finished request_id=%s path=%s status_code=%s duration_ms=%s',
        request_id,
        request.url.path,
        response.status_code,
        duration_ms,
    )
    response.headers['x-request-id'] = request_id
    return response


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    detail = exc.detail if isinstance(exc.detail, str) else 'request failed'
    return JSONResponse(status_code=exc.status_code, content={'detail': detail})


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    request_id = getattr(request.state, 'request_id', 'unknown')
    logger.exception('event=unhandled_exception request_id=%s path=%s', request_id, request.url.path)
    return JSONResponse(status_code=500, content={'detail': 'internal server error'})


app.include_router(health_router)
app.include_router(docs_router)
app.include_router(graph_router)
