import math


class DistanceCalculator:
    EQUATORIAL_EARTH_RADIUS = 6378.1370
    DEG_TO_RAD = math.pi / 180
    DEG_TO_KM = DEG_TO_RAD * EQUATORIAL_EARTH_RADIUS

    @staticmethod
    def distance(lat1: float, lan1: float, lat2: float, lon2: float) -> float:
        dLat = (lat2 - lat1) * DistanceCalculator.DEG_TO_RAD
        dLon = (lon2 - lan1) * DistanceCalculator.DEG_TO_RAD

        a = math.pow(math.sin(dLat / 2), 2) + math.cos(lat1 * DistanceCalculator.DEG_TO_RAD) * \
            math.cos(lat2 * DistanceCalculator.DEG_TO_RAD) * \
            math.pow(math.sin(dLon / 2), 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = DistanceCalculator.EQUATORIAL_EARTH_RADIUS * c

        return d * 1000  # meters

    @staticmethod
    def distance_to_line(point_lat: float, point_lon: float, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        d0 = DistanceCalculator.distance(point_lat, point_lon, lat1, lon1)
        d1 = DistanceCalculator.distance(lat1, lon1, lat2, lon2)
        d2 = DistanceCalculator.distance(point_lat, point_lon, lat2, lon2)

        if d0 ** 2 > d1 ** 2 + d2 ** 2:
            return d2

        if d2 ** 2 > d1 ** 2 + d0 ** 2:
            return d0

        half_p = (d0 + d1 + d2) * 0.5
        area = math.sqrt(half_p * (half_p - d0) *
                         (half_p - d1) * (half_p - d2))
        return 2 * area / d1
