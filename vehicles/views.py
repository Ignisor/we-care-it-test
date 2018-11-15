from django.views.generic import ListView

from vehicles.forms import DatesGapForm
from vehicles.models import Vehicle


class VehicleDistanceListView(ListView):
    model = Vehicle

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VehicleDistanceListView, self).get_context_data(object_list=object_list, **kwargs)
        date_data = {
            "date_from": self.request.GET.get('date_from'),
            "date_to": self.request.GET.get('date_to')
        }
        context['form'] = DatesGapForm(initial=date_data)
        context.update(date_data)
        return context
