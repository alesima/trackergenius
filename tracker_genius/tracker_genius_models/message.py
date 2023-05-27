from django.db import models
from tracker_genius_models.device import Device
from tracker_genius_models.extended import ExtendedModel


class Message(ExtendedModel):
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    type = models.CharField(max_length=32)

    class Meta:
        abstract = True
