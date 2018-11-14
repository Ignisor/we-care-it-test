from django.conf import settings
from django.db import models


class Journey(models.Model):
    timestamp = models.DateTimeField(help_text='journey date and time')
    vehicle = models.ForeignKey('vehicles.Vehicle', related_name='journeys', on_delete=models.PROTECT)
    passengers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='journeys')
    distance = models.PositiveIntegerField(help_text='distance of journey in kilometers')
