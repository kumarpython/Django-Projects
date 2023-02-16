from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Post
from .form import PostCreateForm


@login_required
def list(request):
    pic=request.user.userprofile.pic.url
    posts=Post.objects.filter(approved=True).order_by('-on')
    if request.method=='POST':
        pform=PostCreateForm(request.POST,request.FILES)
        if pform.is_valid():
            post=pform.save(commit=False)
            post.author=request.method.user.id
            post.save(commit=True)
            messages.sucess(request,'Posted Successfully')
            return redirect('post:home')
        else:
            for msg in pform.error_messages :
                messages.error(request, pform.error_messages[msg])
    else:
        pform=PostCreateForm()
        return render(request,'post/list.html',{'posts':posts,'form':pform,'pic':pic})


@login_required
def detail(request,id):
    pic = request.user.userprofile.pic.url
    post=Post.objects.get(pk=id)
    return render(request,'post/detail.html',{'post':post,'pic':pic})


@login_required
def edit (request,id):
    instance=Post.objects.get(pk=id)
    if request.user==instance.author:
        if request.method=='POST':
            pform=PostCreateForm(request,request.FILES,instance=instance)
            if pform.is_valid():
                pform.save()
                return redirect('post:home')
            else :
                for msg in pform.error_messages :
                    messages.error(request, pform.error_messages[msg])
        else :
            pform = PostCreateForm(instance=instance)
    else:
        messages.error(request,'Only Post Author can perform this action')
    return render(request, 'post/edit.html', {'form' : pform})


@login_required
def delete(request,id):
    instance=Post.objects.get(pk=id)
    if request.user == instance.author :
        instance.delete()
    else:
        messages.error(request,'Only Post Author can perform this action')
    return redirect('post:home')