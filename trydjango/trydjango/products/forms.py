from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Your Title'}))

    class Meta:
        model=Product
        fields=['title','description','price','summary','featured']


class RawProductForm(forms.Form):
    title=          forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder':'Your Title'}))
    description=    forms.CharField(required=False,widget=forms.Textarea(attrs={'placeholder':'Your Description','rows':20,'cols':100}))
    price=          forms.DecimalField(initial=199.99)

