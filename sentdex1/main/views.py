from django.shortcuts import render,redirect
from .models import Tutorial, TutorialSeries, TutorialCategory
from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages


def single_slug(request, single_slug):
    # check to see if the url is in categories.
    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)
        series_urls = {}

        for m in matching_series.all():
            part_one = Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest("tutorial_published")
            series_urls[m] = part_one.tutorial_slug

        return render(request=request,template_name='main/category.html',context={"tutorial_series": matching_series, "part_ones": series_urls})
    else:
        # check to see if the url is in tutorials.
        tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
        if single_slug in tutorials:
            this_tutorial = Tutorial.objects.get(tutorial_slug=single_slug)
            tutorials_from_series = Tutorial.objects.filter(tutorial_series__tutorial_series=this_tutorial.tutorial_series).order_by('tutorial_published')
            this_tutorial_idx = list(tutorials_from_series).index(this_tutorial)
            return render(request=request,template_name='main/tutorial.html',context={"tutorial":this_tutorial,"sidebar": tutorials_from_series,"this_tut_idx": this_tutorial_idx})


def register(request):
    form = UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'New Account has been successfully created for {username}')
            login(request,user)
            messages.info(request, f'You are now logged in as {username}')
            return redirect('/')
        else:
            for msg in form.error_messages:
                messages.error(request,f'{msg}:{form.error_messages[msg]}')
    return render(request,'main/register.html',{'form':form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
        template_name = "main/login.html",context={"form":form})


def homepage(request):
    return render(request=request,template_name='main/post_list.html',context={'tutorial':Tutorial.objects.all(), 'categories':TutorialCategory.objects.all(),'series':TutorialSeries.objects.all()})
