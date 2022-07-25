from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Customer, CustomerAddress


class CustomerCreationForm(UserCreationForm):

    class Meta:
        model = Customer
        fields = ['email','fname','lname']


class CustomerChangeForm(UserChangeForm):

    class Meta:
        model = Customer
        fields = ['email','fname','lname','pic','mobile']

    class CustomerAddressForm(forms.ModelForm):
        class Meta:
            model=CustomerAddress
            fields='__all__'