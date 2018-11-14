import datetime

from django import forms

from journeys.models import Journey


class JourneyForm(forms.ModelForm):
    class Meta:
        model = Journey
        fields = '__all__'
        widgets = {
            'timestamp': forms.SelectDateWidget(years=range(1999, datetime.date.today().year + 10)),
        }
