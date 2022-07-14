from django import forms
from django.forms import ModelForm
from .models import Venue,Event


class VenueForm(ModelForm):
    class Meta:
        model=Venue
        fields='__all__'


class EventForm(ModelForm):
    class Meta:
        model=Event
        fields='__all__'
