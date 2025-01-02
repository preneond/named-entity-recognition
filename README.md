# Named Entity Recognition

## Overview

This project automates the extraction of product specifications—such as brand names, storage capacities, and colors—from unstructured data (titles, descriptions, etc.). The solution includes a Named Entity Recognition (NER) model built with FastAPI for the API, and Poetry for dependency management and packaging.

## Goals

1. **Improve Seller Experience**: Automatically extract key product attributes (brand, storage capacity, color) from unstructured data, reducing manual input.
2. **Data Transformation**: Convert the provided dataset into a suitable format for NER model training.
3. **Model Training and Evaluation**: Train and evaluate a model that recognizes product-specific entities.
4. **Data Extraction Enhancement**: Suggest and implement improvements on the naive string matching approach previously used for data extraction.
5. **Dockerization**: Provide a Dockerized setup for easy deployment.
6. **Unit Testing**: Ensure solution reliability through comprehensive unit tests.

### Optional
- **Integration Testing**: Include an integration test for the API route, if needed.

## Files

- **ds_ner_test_case.csv**: Dataset containing product information for model training and testing.
- **README.md**: Project documentation (this file).
- **Dockerfile**: Instructions for building a Docker image of the project.
- **pyproject.toml**: Poetry configuration for dependencies and project settings.
- **src/**: Source code directory (FastAPI endpoints, model training logic, etc.).
- **tests/**: Directory containing unit (and optional integration) tests.

## Setup and Installation

### Prerequisites

- [Docker](https://www.docker.com/get-started) installed.
- [Python 3.11+](https://www.python.org/) installed.
- [Poetry](https://python-poetry.org/docs/) for dependency management.

### Steps

1. **Clone the repository**:
   ```bash
   git clone <repository_link>
   cd product-attribute-extraction

## Setup and Installation

### Prerequisites

- [Docker](https://www.docker.com/get-started) installed.
- A working installation of [Python 3.11+](https://www.python.org/).
- [Poetry](https://python-poetry.org/docs/) installed for dependency management.

### Steps

1. **Clone the repository**:
   ```bash
   git clone <repository_link>
   cd product-attribute-extraction
   ```

2. **Install dependencies using Poetry**:
   ```bash
   poetry install
   ```

3. **Activate the Poetry environment**:
   ```bash
   poetry shell
   ```

4. **Run the FastAPI application**:
   ```bash
   uvicorn src.named_entity_recognition.main:app --reload
   ```

   The API will be available at `http://localhost:8000`.

### Running with Docker

1. **Build the Docker image**:
   ```bash
   docker build -t product-attribute-extraction .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -p 8000:8000 product-attribute-extraction
   ```

   The application will be available at `http://localhost:8000`.

## API Endpoints

- `POST /extract`: This endpoint accepts product descriptions and returns the recognized brands, storage capacities, and colors.

## Data Preparation

The `ds_ner_test_case.csv` file should be pre-processed before training the Named Entity Recognition (NER) model. This involves cleaning the data and transforming it into a format that can be used by the model.

## How This Solution Improves the Onboarding Experience

- **Automatic Data Extraction**: Reduces the manual effort required to enter product details by automatically extracting attributes like brand, storage capacity, and color from product descriptions.
- **Improved Accuracy**: Increases the accuracy of extracted attributes, reducing the risk of errors during the product onboarding process.
- **Streamlined Workflow**: Accelerates the product onboarding process, allowing users to focus on other important tasks.

## Unit and Integration Tests

The project includes unit tests to verify the functionality of key components and optional integration tests to verify the API routes. You can run the tests using the following command:

```bash
pytest tests -s
```

## Dockerization

The entire solution can be packaged into a Docker container to ensure consistent setup and easy deployment. The provided `Dockerfile` builds the project and serves the FastAPI application inside a container.

## Future Improvements

- **Enhanced Data Preprocessing**: The current string matching approach for entity extraction could be improved by using more sophisticated NLP techniques or external knowledge bases.
- **Additional Entity Recognition**: The model can be extended to extract more product attributes, such as dimensions or weight.
