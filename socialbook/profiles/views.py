from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import RegisterUser,ProfileForm
from .models import UserProfile,Friendship


def register(request):
    if request.method=='POST':
        form=RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successful ... Now fill your Profile')
            username=form.cleaned_data.get('username')
            password= form.cleaned_data.get('password2')
            user=authenticate(username=username, password=password)
            login(request, user)
            messages.info(request, f'Logged In as {username}')
            return redirect('profiles:create')
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
    else:
        form=RegisterUser()
        return render(request,'profiles/register.html',{'form':form})


def login_user(request):
    if request.method=="POST":
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,'Login Successful')
            return redirect('profiles:profile',id=request.user.id)
        else :
            messages.error(request, "Invalid username or password.")
    else:
        form=AuthenticationForm()
        return render(request,'profiles/login.html',{'form':form})


def logout_user(request):
    logout(request)
    messages.success(request,'Logout Successful')
    return redirect('profiles:login')


def create_profile(request):
    if request.method=='POST':
        pform=ProfileForm(request.POST,request.FILES)
        if pform.is_valid():
            profile=pform.save(commit=False)
            profile.user=request.user
            # profile.ip=request.META.REMOTE_ADDR
            # profile.mac=request.META.REMOTE_HOST
            # profile.pic=request.cleaned_data.get('pic').open().thumbnail((200,200))
            profile.save()
            messages.success(request,'Profile Saved')
            return redirect('post:home')
        else:
            for msg in pform.error_messages :
                messages.error(request, pform.error_messages[msg])
    else:
        pform=ProfileForm()
        return render(request,'profiles/create.html',{'form':pform})


@login_required
def profile(request,id):
    if request.method=='POST':
        send = request.user.id
        sender = User.objects.get(id=send)
        receive = request.POST['Add Friend']
        receiver=User.objects.get(id=receive)
        friend_request, created = Friendship.objects.get_or_create(sender=sender, receiver=receiver, accepted=False)
        if created :
            messages.success(request, 'Friend Request Sent')
        else :
            messages.error(request, 'Friend Request Already Sent')
    return render(request,'profiles/profile.html',{'instance':UserProfile.objects.get(pk=id)})


@login_required
def edit_profile(request,id):
    instance=UserProfile.objects.get(pk=id)
    if request.user == instance.user:
        if request.method=='POST':
            pform=ProfileForm(request.POST,instance=instance)
            if pform.is_valid():
                profile=pform.save(commit=False)
                profile.user = request.user
                profile.ip = request.META.REMOTE_ADDR
                profile.mac = request.META.REMOTE_HOST
                profile.pic = request.cleaned_data.get('pic').open().thumbnail((200, 200))
                profile.save()
                messages.success(request, 'Profile Saved')
                return redirect('profiles:profile')
            else :
                for msg in pform.error_messages :
                    messages.error(request, pform.error_messages[msg])
        else :
            pform=ProfileForm(instance=instance)
    else:
        messages.error(request,'Only Right User can perform this action')
    return render(request,'profiles/edit.html',{'form':pform,'pic':instance.pic.url,'instance':instance})


@login_required
def friends(request,id):
    instance = UserProfile.objects.get(pk=id)
    accepted=Friendship.objects.filter(receiver=id,accepted=True)
    pending=Friendship.objects.filter(receiver=id,accepted=False)
    return render(request,'profiles/friends.html',{'pic': instance.pic.url,'accepted': accepted, 'pending':pending})




