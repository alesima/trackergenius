from django.db import models
from django.utils.translation import gettext_lazy as _
from tracker_genius_models.category import Category
from tracker_genius_models.extended import ExtendedModel
from tracker_genius_models.model import Model
from tracker_genius_models.position import Position


class Device(ExtendedModel):

    STATUS_UNKNOWN = 'unknown'
    STATUS_ONLINE = 'online'
    STATUS_OFFLINE = 'offline'

    name = models.CharField(max_length=128)
    imei = models.CharField(max_length=32, unique=True),
    status = models.CharField(max_length=32, default=STATUS_OFFLINE, choices=(
        (STATUS_UNKNOWN, _('Unknown')),
        (STATUS_ONLINE, _('Online')),
        (STATUS_OFFLINE, _('Offline')),
    )),
    last_update = models.DateTimeField(null=True, blank=True),
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    disabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name
