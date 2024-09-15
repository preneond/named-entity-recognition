from enum import StrEnum, auto
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel


class LogLevels(StrEnum):
    """Enum of permitted log levels."""

    debug = auto()
    info = auto()
    warning = auto()
    error = auto()
    critical = auto()


class UvicornSettings(BaseModel):
    """Settings for uvicorn server"""

    host: str
    port: int
    log_level: LogLevels
    reload: bool


class ApiConfigSettings(BaseModel):
    """Settings for FastAPI Server"""

    title: str = ""
    description: str = ""
    version: str
    docs_url: str


class Settings(BaseModel):
    uvicorn: UvicornSettings
    api_config: ApiConfigSettings
    ner_model_path: str


def load_from_yaml() -> Any:
    with (Path(__file__).parents[2] / "app_settings.yaml").open() as fp:
        return yaml.safe_load(fp)


@lru_cache
def get_settings() -> Settings:
    yaml_config = load_from_yaml()
    return Settings(**yaml_config)
