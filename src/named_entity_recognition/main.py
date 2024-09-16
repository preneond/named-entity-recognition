import logging
from contextlib import asynccontextmanager
from pathlib import Path

import spacy
import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from starlette import status
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse

from named_entity_recognition.config import get_settings
from named_entity_recognition.responses import error_response


class ProductDescription(BaseModel):
    title: str


@asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    # Load the model once during startup
    # global ner_model
    logging.info("Loading the model...")
    app.state.model = spacy.load(Path.cwd() / settings.ner_model_path)
    logging.info("Model loaded successfully!")
    # Yield control to the application
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
    logger = request.app.state.logger
    logger.error(f"{exc}")
    return error_response(errors=str(exc), status_code=status.HTTP_400_BAD_REQUEST)


class ExtractedProductInformation(BaseModel):
    brand: str | None = None
    storage_capacity: str | None = None
    color: str | None = None


@app.post("/extract", response_class=HTMLResponse)
async def extract(request: Request, description: ProductDescription) -> JSONResponse:
    """
    Uses the NER model to extract information from the product description.
    :param description: The product description.
    :return: The recognized brands, storage capacities, and colors.
    """
    model = request.app.state.model

    # Apply the NER model on the input description
    doc = model(description.title)
    # Initialize empty variables for brand, storage capacity, and color
    brand, storage_capacity, color = None, None, None
    # Extract entities from the doc and categorize them
    for ent in doc.ents:
        if ent.label_ == "Brand":
            brand = ent.text
        elif ent.label_ == "Storage":
            storage_capacity = ent.text
        elif ent.label_ == "Color":
            color = ent.text
    # Create the response with the extracted information
    extracted_info = ExtractedProductInformation(
        brand=brand, storage_capacity=storage_capacity, color=color
    )
    # Return the result as a JSON response
    return JSONResponse({"success": True, "data": extracted_info.model_dump()})


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
