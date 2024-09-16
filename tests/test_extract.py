import pytest
from named_entity_recognition.config import get_ner_model
from spacy.language import Language


@pytest.fixture(scope="module")
def ner_model() -> Language:
    return get_ner_model()


@pytest.mark.parametrize(
    "title",
    [
        "Western Digital My Book Studio 3TB USB 3.0",
        "Samsung Galaxy S21 Ultra 5G 128GB Phantom Black",
        "Toshiba Satellite Pro C70-B",
    ],
)
def test_spacy_model(ner_model: Language, title: str) -> None:
    # Load the spaCy model (replace with your model's path)
    # Test sentence (title)
    # Run the model on the test sentence
    doc = ner_model(title)

    # Extract the recognized entities
    result: dict[str, str | None] = {"Brand": None, "Storage": None, "Color": None}
    for ent in doc.ents:
        if ent.label_ in result:
            result[ent.label_] = ent.text

    # Check if the recognized entities match the expected results
    assert any(result.values()), f"No entities found in '{title}'"
