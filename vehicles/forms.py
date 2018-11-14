import datetime

from django import forms

YEARS_RANGE = range(1999, datetime.date.today().year + 10)


class DatesGapForm(forms.Form):
    date_from = forms.DateField(widget=forms.SelectDateWidget(years=YEARS_RANGE))
    date_to = forms.DateField(widget=forms.SelectDateWidget(years=YEARS_RANGE))
