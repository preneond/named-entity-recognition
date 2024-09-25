# Named  Entity Recognition

## Overview

This project aims to enhance the process of onboarding new products by automating the extraction of product specifications from unstructured data such as product titles and descriptions. The goal is to train a Named Entity Recognition (NER) model capable of identifying specific product attributes like brands, storage capacities (Speicherkapazität), and colors (Farbe). The solution is built using FastAPI for the API implementation, with Poetry for dependency management and packaging.

## Project Objectives

1. **Seller Experience Enhancement**: Develop a solution that improves the product onboarding process by automatically extracting key product attributes from unstructured data.

2. **Data Transformation**: Convert the provided dataset into a suitable format for training an NER model.

3. **Model Training and Evaluation**: Train and evaluate a model for tagging products with recognized brands, storage capacities, and colors.

4. **Data Extraction Improvement**: Suggest improvements for data extraction and preparation, which was initially done using a naive string matching algorithm.

5. **Dockerization**: Provide a Dockerized version of the solution to ensure easy setup and deployment.

6. **Unit Testing**: Implement unit tests to ensure the reliability of the solution.

### Optional
- **Integration Testing**: Implement an integration test for the API route.

## Files

- **ds_ner_test_case.csv**: The provided dataset containing product data used for model training and testing.
- **README.md**: Project documentation (this file).
- **Dockerfile**: Dockerfile to build the project image.
- **pyproject.toml**: Poetry configuration file for dependency management and project settings.
- **src/**: Directory containing the source code, including the API and model training logic.
- **tests/**: Directory containing unit and integration tests.

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
