from django import forms

from journeys.models import Journey


class JourneyForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(
        attrs={
            'type': 'date',
        })
    )

    class Meta:
        model = Journey
        fields = '__all__'
