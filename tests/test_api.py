import httpx
import pytest
from fastapi import status
from fastapi.testclient import TestClient
from named_entity_recognition.config import get_ner_model
from named_entity_recognition.main import app


@pytest.fixture(scope="module")
def client() -> httpx.Client:
    client = TestClient(app)
    client.app.state.model = get_ner_model()  # type: ignore
    return client


@pytest.mark.skip_ci
def test_extract_valid(client: httpx.Client) -> None:
    """
    Test the /extract endpoint with valid input.
    """
    test_data = {"title": "Apple iPhone 12 Pro Max 256GB Silver"}

    # Make a POST request to the /extract endpoint
    response = client.post("/extract", json=test_data)

    # Check that the request was successful
    assert response.status_code == status.HTTP_200_OK

    # Verify that the response contains the expected entities
    response_data = response.json()
    assert "success" in response_data
    assert "data" in response_data
    assert response_data["success"] is True
    assert ["brand", "storageCapacity", "color"] == list(response_data["data"].keys())


@pytest.mark.skip_ci
def test_extract_invalid(client: httpx.Client) -> None:
    """
    Test the /extract endpoint with invalid input.

    """
    test_data = {"title": 12345}

    # Make a POST request to the /extract endpoint with invalid input
    response = client.post("/extract", json=test_data)

    # Check that the request failed
    assert response.status_code == status.HTTP_400_BAD_REQUEST
