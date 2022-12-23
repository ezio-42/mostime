import json
import os
from dataclasses import dataclass


@dataclass
class Config:
    """Configuration for the app."""

    port: int
    app_name: str
    visits_file: str


_default_config_data = {
    "port": 8080,
    "app_name": "app_python",
    "visits_file": "/app/data/visits.txt",
}

_default_config_file = "/app/config.json"

config_file = os.environ.get("CONFIG_FILE", _default_config_file)

try:
    with open(config_file, "r") as f:
        data = json.load(f)
        _default_config_data.update(data)
except FileNotFoundError:
    pass

default_config = Config(**_default_config_data)  # type: ignore
