import datetime
from calendar import HTMLCalendar
import csv

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import VenueForm, EventForm
from .models import Event, Venue


def home(request, year=datetime.date.today().year, month=datetime.date.today().month) :
    cal = HTMLCalendar().formatmonth(year, month)
    curr_yr = datetime.date.today().year
    return render(request, 'events/base.html',
                  {'name' : request.user, 'year' : year, 'month' : month, 'cal' : cal,
                   'time' : datetime.time().strftime('%I:%M %p'), 'curr_yr' : curr_yr,
                   'events' : Event.objects.filter(date__year=year,date__month=month)})


def cal(request, year, month) :
    # month_number = int(list(calendar.month_name).index(month.title()))
    cal = HTMLCalendar().formatmonth(year, month)
    curr_yr = datetime.date.today().year
    return render(request, 'events/base.html',
                  {'name' : request.user, 'year' : year, 'month' : month, 'cal' : cal,
                   'time' : datetime.time().strftime('%I:%M %p'), 'curr_yr' : curr_yr})


def approval(request):
    if request.user.is_superuser:
        if request.method=="POST":
            id=request.POST['boxes']
            Event.objects.filter(pk=int(id)).update(approved=True)
            messages.success(request,'Approved')
            return redirect('events:events')
        else:
            messages.error(request,'Error Approving!')
    else:
        messages.error(request,'Restricted, only admins')
        return redirect('/')
    return render(request,'events/approval.html',{'events':Event.objects.all()})

# --------------------------------------- Venue -----------------------------------------


def venue_event(request,id):
    # venue=Venue.objects.filter(pk=id)
    events_list=Event.objects.filter(venue__pk=id)
    # events_list=venue.event_set.all()
    return render(request,'events/venue_event.html',{'events':events_list})


def addvenue(request) :
    if request.method == "POST" :
        form = VenueForm(request.POST,request.FILES)
        if form.is_valid() :
            venue=form.save(commit=False)
            venue.owner=request.method.user.id
            venue.save()
            messages.success(request, 'New Venue Added Successfully')
            return redirect('')
        else :
            for msg in form.error_messages :
                messages.error(request, form.error_messages[msg])
    else :
        form = VenueForm()
        return render(request, 'events/venue_add.html', {'form' : form})


def venues(request) :
    return render(request, 'events/venue_list.html', {'venues' : Venue.objects.all().order_by('name')})


def indvenue(request, id) :
    return render(request, 'events/venue.html', {'venue' : Venue.objects.get(pk=id)})


def editvenue(request, id) :
    instance = Venue.objects.get(pk=id)
    if request.method == "POST" :
        form = VenueForm(request.POST,request.FILES, instance=instance)
        if form.is_valid() :
            form.save()
            messages.success(request, 'New Venue Added Successfully')
            return redirect('events:venues')
        else :
            for msg in form.error_messages :
                messages.error(request, form.error_messages[msg])
    else :
        form = VenueForm(instance=instance)
        return render(request, 'events/venue_edit.html', {'form' : form})


def deletevenue(request, id) :
    if go :
        instance = Venue.objects.get(pk=id)
        instance.delete()
        return redirect('events:venues')
    else :
        return render(request, 'events/venue_delete.html', {'venue' : Venue.objects.get(pk=id)})


def searchvenue(request) :
    if request.method == 'POST' :
        query = request.POST['query']
        results = Venue.objects.filter(name__contains=query)
        return render(request, 'events/venue_search.html', {'query' : query, 'results' : results})
    else :
        return render(request, 'events/venue_search.html', {})

# -------------------------------------- Event--------------------------------------------


def addevent(request) :
    if request.method == "POST" :
        form = EventForm(request.POST,request.FILES)
        if form.is_valid() :
            form.save()
            messages.success(request, 'New Event Added Successfully')
            return redirect('events:events')
        else :
            for msg in form.error_messages :
                messages.error(request, form.error_messages[msg])
    else :
        form = EventForm()
        return render(request, 'events/event_add.html', {'form' : form})


def events(request) :
    # p = Paginator(Event.objects.all())
    # page = request.GET.get('page')
    # event = p.get_page(page)
    return render(request, 'events/event_list.html', {'events' : Event.objects.all()})


def indevent(request, id) :
    return render(request, 'events/event.html', {'event' : Event.objects.get(pk=id)})


def editevent(request, id) :
    instance = Event.objects.get(pk=id)
    if request.method == "POST" :
        form = EventForm(request.POST,request.FILES, instance=instance)
        if form.is_valid() :
            form.save()
            messages.success(request, 'New Venue Added Successfully')
            return redirect('events:venues')
        else :
            for msg in form.error_messages :
                messages.error(request, form.error_messages[msg])
    else :
        form = EventForm(instance=instance)
        return render(request, 'events/event_edit.html', {'form' : form})


def deleteevent(request, id) :
    if go :
        instance = Event.objects.get(pk=id)
        if request.user==instance.manager:
            instance.delete()
        else:
            messages.error(request,f'Event Manager : {instance.manager} , only {instance.manager} can Delete')
        return redirect('events:events')
    else :
        return render(request, 'events/event_delete.html', {'event' : Event.objects.get(pk=id)})


def searchevent(request) :
    if request.method == 'POST' :
        query = request.POST['query']
        results = Event.objects.filter(name__contains=query)
        return render(request, 'events/event_search.html', {'query' : query, 'results' : results})
    else :
        return render(request, 'events/event_search.html', {})

# -------------------------------------- Files ----------------------------------------------

def venuetext(request) :
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=venues.txt'
    # Designate The Model
    venues = Venue.objects.all()

    # Create blank list
    lines = []
    # Loop Thu and output
    for venue in venues :
        lines.append(f'Name: {venue.name}\nAddress: {venue.address}\nPhone: {venue.phone}\nEMail: {venue.email}\n')

    # Write To TextFile
    response.writelines(lines)
    return response


# Generate CSV File Venue List
def venuecsv(request) :
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=venues.csv'

    # Create a csv writer
    writer = csv.writer(response)

    # Designate The Model
    venues = Venue.objects.all()

    # Add column headings to the csv file
    writer.writerow(['Venue Name', 'Address', 'Zip Code', 'Phone', 'Web Address', 'Email'])

    # Loop Thu and output
    for venue in venues :
        writer.writerow([venue.name, venue.address, venue.phone, venue.email])

    return response
