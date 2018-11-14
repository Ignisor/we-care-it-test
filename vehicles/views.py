import datetime

from django.views.generic import ListView

from vehicles.forms import DatesGapForm
from vehicles.models import Vehicle


class VehicleDistanceListView(ListView):
    model = Vehicle

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VehicleDistanceListView, self).get_context_data(object_list=object_list, **kwargs)
        context['form'] = DatesGapForm()
        date_from_dict = {k: v for k, v in self.request.GET.items() if 'date_from' in k}
        context['date_from'] = VehicleDistanceListView.date_dict_to_iso(date_from_dict)
        date_to_dict = {k: v for k, v in self.request.GET.items() if 'date_to' in k}
        context['date_to'] = VehicleDistanceListView.date_dict_to_iso(date_to_dict)

        return context

    @staticmethod
    def date_dict_to_iso(date_dict):
        try:
            return datetime.date(**{k.split('_')[-1]: int(v) for k, v in date_dict.items()}).isoformat()
        except TypeError:
            return None
