from django.contrib.auth.models import User
from django.db import models


@property
def distances(self):
    return self.journeys.values_list('vehicle__registration_number').order_by('vehicle__registration_number')\
        .annotate(total=models.Sum('distance'))


User.add_to_class("distances", distances)

