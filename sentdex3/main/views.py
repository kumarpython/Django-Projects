from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Tutorial, Category,Series
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import NewUserCreationForm


def ss(request,ss):
    ser=[s.series for s in Series.objects.all() if series_category__category_slug==ss ]
    return render(request,'main/series.html',{'series':ser})


def homepage(request):
    return render(request,'main/home.html',{'category':Category.objects.all})


def register(request):
    if request.method=='POST':
        form=NewUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'New Account Created for {username}!')
            login(request,user)
            messages.info(request, f'Logged In as :{username}!')
            return redirect('main:homepage')
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
    else:
        form = NewUserCreationForm()
        return render(request,'main/register.html',{'form':form})


def logout_user(request):
    logout(request)
    messages.info(request,'Logout Successful')
    return redirect('main:homepage')


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('main:homepage')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,template_name = "main/login.html",context={"form":form})