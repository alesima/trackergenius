from tracker_genius.tracker_genius_models.geofence import Geofence
from tracker_genius_helpers.distance_calculator import DistanceCalculator
from tracker_genius_geofence.geometry import GeofenceGeometry
from django.conf import settings
from typing import List


class GeofencePolyline(GeofenceGeometry):
    coordinates: List[GeofenceGeometry.Coordinate]

    def __init__(self):
        self.coordinates = []

    def contains_point(self, geofence: Geofence, latitude: float, longitude: float) -> bool:
        distance = settings.GEOFENCE_POLYLINE_DISTANCE

        for i in range(1, len(self.coordinates)):
            if DistanceCalculator.distance_to_line(
                latitude,
                longitude,
                self.coordinates[i - 1].lat,
                self.coordinates[i - 1].lon,
                self.coordinates[i].lat,
                self.coordinates[i].lon
            ) <= distance:
                return True

            return False

    def calculate_area(self) -> float:
        return 0

    def to_wtk(self) -> str:
        wtk = "LINESTRING ("

        for coordinate in self.coordinates:
            wtk += f"{coordinate.lat} {coordinate.lon}, "

        return wtk[:-2] + ")"

    def from_wkt(self, wkt: str) -> None:
        self.coordinates = []

        if not wkt.startswith("LINESTRING"):
            raise Exception("Mismatch geometry type")

        content = wkt[wkt.index("(") + 1: wkt.index(")")]

        if not content:
            raise ValueError("No content")

        comma_tokens = content.split(",")

        if len(comma_tokens) < 2:
            raise ValueError("No valid content")

        for comma_token in comma_tokens:
            tokens = comma_token.strip().split(" ")

            if len(tokens) != 2:
                raise ValueError(
                    f"Here must be two coordinates: {comma_token}")

            try:
                latitude = float(tokens[0])
                longitude = float(tokens[1])
            except ValueError:
                raise ValueError(f"Coordinates must be float values")

            coordinate = self.Coordinate(latitude, longitude)
            self.coordinates.append(coordinate)
