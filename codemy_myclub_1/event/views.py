from django.http import HttpResponse
from django.shortcuts import redirect, render
import calendar
from calendar import HTMLCalendar
import datetime
from .models import Events,Venue
from .forms import VenueForm,EventsForm
import csv

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


def home(request,year=datetime.date.today().year,monthn=datetime.date.today().month):
    cal= HTMLCalendar().formatmonth(year,monthn)
    month = calendar.month_name[monthn]
    return render(request,'event/home.html', {'month':month,'year':year,'cal':cal, 'year':year})


def next(request,monthn, year):
    cal= HTMLCalendar().formatmonth(year,monthn)
    month = calendar.month_name[monthn]
    return render(request,'event/home.html', {'month':month,'year':year,'cal':cal, 'year':year})


def search(request):
    if request.method =='POST':
        quer = request.POST['query']
        results = Venue.objects.filter(name__contains=quer)
        return render(request, 'event/search.html', {'query':quer,'results':results})
    else:
        return render(request,'event/search.html',{})


# Generate TXT file
def venuestxt(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=venues.txt'
    venues = Venue.objects.all()
    lines =[]
    for venue in venues:
        lines.append(f'Name: {venue.name}/n Address: {venue.address}/n Phone: {venue.phone}/n Website: {venue.web}/n Email: {venue.email}')
    response.writelines(lines)
    return response


# Generate CSV file
def venuescsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=venues.csv'

    writer = csv.writer(response)

    venues = Venue.objects.all()

    # Heading Row
    writer.writerow(['name','address','phone','website', 'email'])

    for venue in venues:
        writer.writerow([venue.name, venue.address, venue.address, venue.phone, venue.web, venue.email])
    return response


# Generate PDF file
def venuespdf(request):
    # Create a Bytesize object
    buffer = io.BytesIO()

    # Create a Canvas object
    c = canvas.Canvas(buffer,pagesize=letter, bottomup=0)

    # Create a Text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    venues = Venue.objects.all()
    lines =[]
    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.address)
        lines.append(venue.phone)
        lines.append(venue.web)
        lines.append(venue.email)
        lines.append(" ")

    # Loop
    for line in lines :
        textob.textLine(line)

    # Finish Up
    c.drawText(textob)
    c.showPage()
    c.save()
    buffer.seek(0)

    # Return something
    return FileResponse(buffer, as_attachment=True, filename='venues.pdf')

# ---------------------- EVENT RELATED METHODS --------------------


def all_events(request):
    list_events = Events.objects.all().order_by('-event_date')
    return render(request,'event/event_list.html', {'events': list_events})


def indevent(request,id):
    event = Events.objects.get(pk=id)
    return render(request,'event/event_ind.html',{'event': event})


def event_add(request):
    if request.method == 'POST':
        form = EventsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events')
    else:
        form = EventsForm()
    return render(request,'event/event_add.html', {'form': form})


def event_edit(request,id):
    event = Events.objects.get(pk=id)
    form = EventsForm(request.POST or None, instance = event)
    if form.is_valid() :
        form.save()
        return redirect('events')
    return render(request,'event/event_edit.html',{'event': event,'form': form})


def event_delete(request,id):
    event = Events.objects.get(pk=id)
    if request.method == 'POST':
        event.delete()
        redirect('events')
    else:
        return render(request,'event/event_delete.html',{'event': event})


# ---------------------- VENUE RELATED METHODS --------------------

def venue_all(request):
    list_venue = Venue.objects.all()
    return render(request,'event/venue_list.html', {'venues': list_venue})


def indvenue(request,id):
    venue = Venue.objects.get(pk=id)
    return render(request,'event/venue_ind.html',{'venue': venue})


def venue_add(request):
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venues')
    else:
        form = VenueForm()
    return render(request,'event/venue_add.html', {'form': form})


def venue_edit(request,id):
    venue = Venue.objects.get(pk=id)
    form = VenueForm(request.POST or None, instance = venue)
    if form.is_valid() :
        form.save()
        return redirect('venues')
    return render(request,'event/venue_edit.html',{'venue': venue,'form': form})


def venue_delete(request,id):
    venue = Venue.objects.get(pk=id)
    if request.method == 'POST':
        venue.delete()
        redirect('events')
    else:
        return render(request,'event/venue_delete.html',{'venue': venue})
