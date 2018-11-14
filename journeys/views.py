from django.views.generic import CreateView

from journeys.models import Journey


class JourneyCreateView(CreateView):
    model = Journey
    fields = '__all__'
