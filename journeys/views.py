from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from journeys.forms import JourneyForm
from journeys.models import Journey


class JourneyCreateView(LoginRequiredMixin, CreateView):
    model = Journey
    form_class = JourneyForm
    success_url = reverse_lazy('index')
