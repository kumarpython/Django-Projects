from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages


def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account Sucessfully Created for {username}!, Please Login')
            return redirect('login')
        else:
            messages.error(request,'New user could not be created due to Errors, Please fix the errors and try again !')

    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if (u_form.is_valid()) & (p_form.is_valid()):
            u_form.save(),p_form.save()
            messages.success(request, 'Profile Info Updated Successfully!')
            return redirect('profile')
        else:
            messages.error(request,'Profile could NOT be updated due to Errors, Please fix and try again !')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request,'users/profile.html',{'u_form':u_form,'p_form':p_form})
