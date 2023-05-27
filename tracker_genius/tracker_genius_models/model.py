from django.db import models
from tracker_genius_models.base import BaseModel


class Model(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
