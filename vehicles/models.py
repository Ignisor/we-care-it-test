from django.db import models


class Vehicle(models.Model):
    registration_number = models.PositiveIntegerField(primary_key=True)
