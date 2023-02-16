from django import forms
from django.forms import ModelForm
from .models import Venue, Events


class DateInput(forms.DateInput):
    input_type = 'date'


class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'


class EventsForm(ModelForm):
    class Meta:
        model = Events
        fields = '__all__'
        widgets = {'event_date' : DateInput()}