from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from journeys.models import Journey


class JourneyCreateView(LoginRequiredMixin, CreateView):
    model = Journey
    fields = '__all__'
