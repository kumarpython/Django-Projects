from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegisterUserForm

def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,f'Login successful for {user} !')
            return redirect('/')
        else:
            messages.error(request,'Please check the credentials again !')
    else:
        return render(request,'members/login.html',{})


def logout_user(request):
    logout(request)
    messages.success(request,'Logout successful!')
    return redirect('/')


def register(request):
    if request.method == "POST" :
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            messages.success(request,f'New Account SUCCESSFULLY created for {username}, logging in')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form=RegisterUserForm()
    return render(request,'members/register.html',{'form':form})