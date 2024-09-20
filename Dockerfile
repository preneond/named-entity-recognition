FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        gcc \
        g++ \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get clean

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Add Python path to PATH
ENV PYTHONPATH="${PYTHONPATH}: /app/src"

# Copy pyproject.toml and poetry.lock to the working directory
COPY pyproject.toml poetry.lock /app/

RUN poetry install --no-root --no-dev

# Copy the application code to the working directory
COPY . /app

EXPOSE 8000

# only ssh for debugging
CMD ["poetry", "run", "uvicorn", "named_entity_recognition.main:app", "--host", "0.0.0.0", "--port", "8000"]
