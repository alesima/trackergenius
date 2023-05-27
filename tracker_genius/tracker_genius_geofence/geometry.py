from abc import ABC, abstractmethod
from tracker_genius_models.geofence import Geofence


class GeofenceGeometry(ABC):
    @abstractmethod
    def contains_point(self, geofence: Geofence, latitude: float, longitude: float) -> bool:
        pass

    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def to_wkt(self) -> str:
        pass

    @abstractmethod
    def from_wkt(self, wkt: str) -> None:
        pass

    class Coordinate:
        def __init__(self, lat: float, lon: float):
            self._lat = lat
            self._lon = lon

        @property
        def lat(self):
            return self._lat

        @lat.setter
        def lat(self, value: float):
            if not -90 <= value <= 90:
                raise ValueError('Latitude must be between -90 and 90')
            self._lat = value

        @property
        def lon(self):
            return self._lon

        @lon.setter
        def lon(self, value: float):
            if not -180 <= value <= 180:
                raise ValueError('Longitude must be between -180 and 180')
            self._lon = value
