from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class RegisterUser(UserCreationForm):
    fname=forms.CharField(max_length=50)
    lname=forms.CharField(max_length=50)
    dob=forms.DateTimeField(required=True,help_text='YYYY-MM-DD')

    class Meta:
        model=User
        fields=['username','password1','password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['fname','lname','gender','email','mobile','married','pic','country','state','city','zipcode']
