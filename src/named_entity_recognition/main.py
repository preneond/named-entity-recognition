import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette import status
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from named_entity_recognition.api_router import router
from named_entity_recognition.config import get_ner_model, get_settings
from named_entity_recognition.responses import error_response


def _setup_logging() -> None:
    logging.basicConfig(
        level=get_settings().uvicorn.log_level.value.upper(),
        format="%(asctime)s | %(levelname)-8s | %(module)s:%(funcName)s:%(lineno)d - %(message)s",  # noqa: E501
    )


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Load the model once during startup
    # global ner_model
    _setup_logging()
    logging.info("Loading the NER model...")
    app.state.model = get_ner_model()
    logging.info("NER nodel loaded successfully!")
    yield


settings = get_settings()
app = FastAPI(
    title=settings.api_config.title,
    description=settings.api_config.description,
    version=settings.api_config.version,
    docs_url=settings.api_config.docs_url,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RequestValidationError)
@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception) -> JSONResponse:
    logging.error(f"{exc}")
    return error_response(errors=str(exc), status_code=status.HTTP_400_BAD_REQUEST)


app.include_router(router)

if __name__ == "__main__":
    settings = get_settings()
    server = settings.uvicorn
    uvicorn.run(
        app="main:app",
        host=server.host,
        port=server.port,
        log_level=server.log_level,
        reload=server.reload,
    )
