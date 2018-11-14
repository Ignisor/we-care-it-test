from django.db import models


class Vehicle(models.Model):
    registration_number = models.PositiveIntegerField(primary_key=True)

    def distance(self, date_from=None, date_to=None):
        journeys = self.journeys.all()

        if date_from:
            journeys = journeys.filter(timestamp__gte=date_from)
        if date_to:
            journeys = journeys.filter(timestamp__lte=date_to)

        return journeys.aggregate(models.Sum('distance')).get('distance__sum') or 0
