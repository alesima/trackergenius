from tracker_genius_models.base import BaseModel
from tracker_genius_models.mixins.extended import ExtendedModelMixin
from typing import Optional


class ExtendedModel(BaseModel, ExtendedModelMixin):
    class Meta:
        abstract = True

    def get_string(self, key: str, default: Optional[str] = None) -> Optional[str]:
        return self.get_attribute(key, default)

    def get_float(self, key: str, default: float = 0.0) -> float:
        value = self.get_attribute(key)
        if isinstance(value, (float, int)):
            return float(value)
        elif isinstance(value, str):
            return float(value)
        return default

    def get_boolean(self, key: str, default: bool = False) -> bool:
        value = self.get_attribute(key)
        if isinstance(value, bool):
            return value
        elif isinstance(value, str):
            return value.lower() in ['true', '1']
        return default

    def get_integer(self, key: str, default: int = 0) -> int:
        value = self.get_attribute(key)
        if isinstance(value, int):
            return value
        elif isinstance(value, str):
            return int(value)
        return default
