from pydantic import BaseModel
from typing import Type, TypeVar

Model = TypeVar("Model", bound=BaseModel)


def load_model(t: Type[Model], o: dict) -> Model:
    populated_keys = o.keys()
    required_keys = set(t.schema()["required"])
    missing_keys = required_keys.difference(populated_keys)
    if missing_keys:
        raise ValueError(f"Required keys missing: {missing_keys}")
    all_definition_keys = t.schema()["properties"].keys()
    return t(**{k: v for k, v in o.items() if k in all_definition_keys})
