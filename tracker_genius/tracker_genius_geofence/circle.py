from math import pi
from tracker_genius.tracker_genius_models.geofence import Geofence
from tracker_genius_geofence.geometry import GeofenceGeometry
from tracker_genius_helpers.distance_calculator import DistanceCalculator


class GeofenceCircle(GeofenceGeometry):
    def __init__(self, latitude: float, longitude: float, radius: float):
        self.center_latitude = latitude
        self.center_longitude = longitude
        self.radius = radius

    def distance_from_center(self, latitude: float, longitude: float) -> float:
        return DistanceCalculator.distance(
            self.center_latitude, self.center_longitude, latitude, longitude
        )

    def contains_point(self, geofence: Geofence, latitude: float, longitude: float) -> bool:
        return self.distance_from_center(latitude, longitude) <= self.radius

    def calculate_area(self) -> float:
        return pi * (self.radius ** 2)

    def to_wkt(self) -> str:
        return f"CIRCLE ({self.center_latitude} {self.center_longitude}, {self.radius})"

    def from_wkt(self, wkt: str) -> None:
        if not wkt.startswith("CIRCLE"):
            raise ValueError("Mismatch geometry type")

        content = wkt[wkt.index("(") + 1: wkt.index(")")]

        if not content:
            raise ValueError("No content")

        comma_tokens = content.split(",")

        if len(comma_tokens) != 2:
            raise ValueError("Not valid content")

        tokens = comma_tokens[0].split(" ")

        if len(tokens) != 2:
            raise ValueError("Too much or less coordinates")

        try:
            self.center_latitude = float(tokens[0])
        except ValueError:
            raise ValueError(f"{tokens[0]} is not a decimal")

        try:
            self.center_longitude = float(tokens[1])
        except ValueError:
            raise ValueError(f"{tokens[1]} is not a decimal")

        try:
            self.radius = int(comma_tokens[1])
        except ValueError:
            raise ValueError(f"{comma_tokens[1]} is not an decimal")
