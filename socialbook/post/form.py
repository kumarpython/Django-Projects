from django import forms
from django.forms import ModelForm
from .models import Post


class PostCreateForm(ModelForm):
    class Meta:
        model= Post
        fields=['text','url','image']


# class ContactForm(forms.Form):
#     sender= forms.EmailField(required=True)
#     matter=forms.Textarea()
#     recieved_on=forms.DateTimeField(auto_now_add=True)