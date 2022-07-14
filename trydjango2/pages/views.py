from django.http import HttpResponse
from django.shortcuts import render


def home_view(request,*args,**kwargs):
    # return HttpResponse('<h1>Hello World<h1>')
    return render(request,'post_list.html',{})


def contact_view(request,*args,**kwargs):
    # return HttpResponse('<h1>Contact Page<h1>')
    return render(request, 'contact.html', {})


def about_view(request,*args,**kwargs):
    # return HttpResponse('<h1>About Page<h1>')
    context={'name':'Subham Das',
             'email':'any@any.com',
             'number':123,
             'list':[1,2,3,4,5,6,7,8,9,10]   }
    return render(request, 'about.html',context)
