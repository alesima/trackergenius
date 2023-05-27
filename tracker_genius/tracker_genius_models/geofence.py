from django.db import models
from tracker_genius_geofence.circle import GeofenceCircle
from tracker_genius_geofence.geometry import GeofenceGeometry
from tracker_genius_geofence.polygon import GeofencePolygon
from tracker_genius_geofence.polyline import GeofencePolyline
from tracker_genius_models.extended import ExtendedModel


class Geofence(ExtendedModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    area = models.TextField()

    @property
    def geometry(self):
        if self.area.startswith('CIRCLE'):
            return GeofenceCircle(self.area)
        elif self.area.startswith('POLYGON'):
            return GeofencePolygon(self.area)
        elif self.area.startswith('LINESTRING'):
            return GeofencePolyline(self.area)
        else:
            raise ValueError('Unknown geometry type')

    @geometry.setter
    def geometry(self, geometry: GeofenceGeometry):
        self.area = geometry.to_wkt()
