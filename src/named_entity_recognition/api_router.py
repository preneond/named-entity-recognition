from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, JSONResponse

from named_entity_recognition.models import (
    ExtractedProductInformation,
    ProductDescription,
)
from named_entity_recognition.responses import success_response

router = APIRouter()


@router.get("/", response_class=JSONResponse)
async def welcome() -> JSONResponse:
    return success_response("🎉")


@router.post("/extract", response_class=HTMLResponse)
async def extract(request: Request, description: ProductDescription) -> JSONResponse:
    """
    Uses the NER model to extract information from the product description.
    :param description: The product description.
    :return: The recognized brands, storage capacities, and colors.
    """
    model = request.app.state.model

    # Apply the NER model on the input description
    model_output = model(description.title)

    extracted_info = ExtractedProductInformation.from_spacy_output(model_output)

    return success_response(extracted_info.model_dump(by_alias=True))
