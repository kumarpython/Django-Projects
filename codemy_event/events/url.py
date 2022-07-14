from django.urls import path
from .views import home, cal,approval, venues, indvenue, addvenue, editvenue, deletevenue, searchvenue, addevent, events, indevent, \
    editevent, deleteevent,searchevent, venuetext, venuecsv,venue_event

app_name = 'events'

urlpatterns = [
    path('', home, name='home'),
    path('<int:year>/<int:month>/', cal, name='cal'),
    path('venues/', venues, name='venues'),
    path('venue/<int:id>/', indvenue, name='indvenue'),
    path('venue/add/', addvenue, name='addvenue'),
    path('venue/<int:id>/edit/', editvenue, name='editvenue'),
    path('venue/<int:id>/delete/', deletevenue, name='deletevenue'),
    path('venue/search/', searchvenue, name='searchvenue'),
    path('venue/text/', venuetext, name='venuetext'),
    path('venue/csv/', venuecsv, name='venuecsv'),
    path('venue/<int:id>/events/', venue_event, name='venue-event'),
    path('events/', events, name='events'),
    path('event/<int:id>/', indevent, name='indevent'),
    path('event/add/', addevent, name='addevent'),
    path('event/<int:id>/edit/', editevent, name='editevent'),
    path('event/<int:id>/delete/', deleteevent, name='deleteevent'),
    path('event/search/', searchevent, name='searchevent'),
    path('event/approval/', approval, name='approval'),
]
