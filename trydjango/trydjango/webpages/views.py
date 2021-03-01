from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args,**kwargs):
    # return HttpResponse('<h1>Home Page</h1>')
    return render(request,'home.html',{})


def about_view(request, *args,**kwargs):
    # return HttpResponse('<h1>About Page</h1>')
    context={
        'name': 'Subham Das',
        'dob':'28-05-1985',
        'pin':700074,
        'family': ['Baba','Ma','Dhruba','Ami']
             }
    return render(request, 'about.html', context)


def contact_view(request, *args,**kwargs):
    # return HttpResponse('<h1>Contact Page</h1>')
    return render(request, 'contact.html', {})

