from shapely.geometry import Polygon
from tracker_genius.tracker_genius_models.geofence import Geofence
from tracker_genius_geofence.geometry import GeofenceGeometry
from tracker_genius_helpers.distance_calculator import DistanceCalculator
from typing import List


class GeofencePolygon(GeofenceGeometry):
    coordinates: List[GeofenceGeometry.Coordinate]

    def __init__(self):
        self.coordinates = []

    def pre_calculate(self):
        if self.coordinates is None:
            return

        poly_corners = len(self.coordinates)
        j = poly_corners - 1

        self.constant = []
        self.multiple = []

        has_negative = False
        has_positive = False

        for i in range(poly_corners):
            if self.coordinates[i].lon > 90:
                has_positive = True
            elif self.coordinates[i].lon < -90:
                has_negative = True

        self.need_normalize = has_positive and has_negative

        for i in range(poly_corners):
            pass

    def normalize_lon(self, lon):
        if self.need_normalize and lon < -90:
            return lon + 360
        return lon

    def contains_point(self, geofence: Geofence, latitude: float, longitude: float) -> bool:
        poly_corners = len(self.coordinates)
        j = poly_corners - 1
        longitude_norm = self.normalize_lon(longitude)
        odd_nodes = False

        for i in range(poly_corners):
            if (self.normalize_lon(self.coordinates[i].lon) < longitude_norm and
                self.normalize_lon(self.coordinates[j].lon) >= longitude_norm) or (self.normalize_lon(self.coordinates[j].lon) < longitude_norm
                                                                                   and self.need_normalize(self.coordinates[i].lon) >= longitude_norm):
                odd_nodes ^= (longitude_norm *
                              self.multiple[i] + self.constant[i]) < latitude
            j = i

        return odd_nodes

    def calculate_area(self) -> float:
        polygon = Polygon(
            [(coord.lat, coord.lon) for coord in self.coordinates]
        )
        return polygon.area * DistanceCalculator.DEG_TO_KM * DistanceCalculator.DEG_TO_KM

    def to_wkt(self) -> str:
        wkt = "POLYGON(("

        for coordinate in self.coordinates:
            wkt += f"{coordinate.lon} {coordinate.lat}, "

        return wkt[:-2] + "))"

    def from_wkt(self, wkt: str) -> None:
        self.coordinates = []

        if not wkt.startswith("POLYGON"):
            raise ValueError("Invalid geometry type")

        content = wkt[wkt.index("((") + 2:wkt.index("))")]

        if not content:
            raise ValueError("No content")

        comma_tokens = content.split(",")

        if len(comma_tokens) < 3:
            raise ValueError("Not valid content")

        for comma_token in comma_tokens:
            tokens = comma_token.strip().split(" ")

            if len(tokens) != 2:
                raise ValueError(
                    f"Here must be two coordinates: {comma_token}")

            try:
                latitude = float(tokens[0])
                longitude = float(tokens[1])
            except ValueError:
                raise ValueError("Coordinates must be float values")

            coordinate = GeofenceGeometry.Coordinate(latitude, longitude)
            self.coordinates.append(coordinate)

        self.pre_calculate()
