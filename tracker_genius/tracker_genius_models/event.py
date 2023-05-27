from django.db import models
from django.utils import timezone
from tracker_genius_models.message import Message


class Event(Message):
    TYPE_COMMAND_RESULT = 'commandResult'
    TYPE_DEVICE_ONLINE = 'deviceOnline'
    TYPE_DEVICE_UNKNOWN = 'deviceUnknown'
    TYPE_DEVICE_OFFLINE = 'deviceOffline'
    TYPE_DEVICE_INACTIVE = 'deviceInactive'
    TYPE_DEVICE_MOVING = 'deviceMoving'
    TYPE_DEVICE_STOPPED = 'deviceStopped'
    TYPE_DEVICE_OVERSPEED = 'deviceOverspeed'
    TYPE_DEVICE_FUEL_DROP = 'deviceFuelDrop'
    TYPE_DEVICE_FUEL_INCREASE = 'deviceFuelIncrease'
    TYPE_GEOFENCE_ENTER = 'geofenceEnter'
    TYPE_GEOFENCE_EXIT = 'geofenceExit'
    TYPE_ALARM = 'alarm'
    TYPE_IGNITION_ON = 'ignitionOn'
    TYPE_IGNITION_OFF = 'ignitionOff'
    TYPE_MAINTENANCE = 'maintenance'
    TYPE_TEXT_MESSAGE = 'textMessage'
    TYPE_DRIVER_CHANGED = 'driverChanged'
    TYPE_MEDIA = 'media'

    ALL_EVENTS = 'allEvents'

    event_time = models.DateTimeField(default=timezone.now)
    position_id = models.BigIntegerField()
    geofence_id = models.BigIntegerField(default=0)
