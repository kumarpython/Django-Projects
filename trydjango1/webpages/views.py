from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    # return HttpResponse('<h1>Hello World</h1>')
    return render(request,'post_list.html',{})


def contact_view(request):
    # return HttpResponse('<h1>Contact Page</h1>')
    return render(request, 'contact.html', {})


def about_view(request):
    context={'text':'Awesome','number':123}
    # return HttpResponse('<h1>About Page</h1>')
    return render(request, 'about.html', context)

