from abc import ABC, abstractmethod
from typing import Optional


class Geocoder(ABC):
    class ReverseGeocoderCallback:
        @abstractmethod
        def on_success(self, address: str):
            pass

        @abstractmethod
        def on_failure(self, e: Exception):
            pass

    @abstractmethod
    def get_address(self, latitude: float, longitude: float, callback: ReverseGeocoderCallback) -> Optional[str]:
        pass

    @abstractmethod
    def set_statitics_manager(self, statistics_manager):
        pass
