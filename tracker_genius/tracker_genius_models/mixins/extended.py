from typing import Optional, Any, Dict


class ExtendedModelMixin:
    def has_attribute(self, key: str) -> bool:
        return hasattr(self, key)

    def set_attribute(self, key: str, value: Any) -> None:
        setattr(self, key, value)

    def get_attribute(self, key: str, default=Optional[Any]) -> Any:
        return getattr(self, key, default)

    def set_attributes(self) -> Dict[str, Any]:
        for key, value in self.dict().items():
            self.set_attribute(key, value)

    def get_attributes(self) -> Dict[str, Any]:
        return {field.verbose_name: self.get_attribute(field.name) for field in self._meta.get_fields() if self.has_attribute(field.verbose_name)}
