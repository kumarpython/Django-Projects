from django.urls import path
from. import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('<int:monthn>/<int:year>/', views.next, name='homespec'),
    path('events/', views.all_events, name='events'),
    path('event/add/', views.event_add, name='event-add'),
    path('event/<int:id>/', views.indevent, name='indevent'),
    path('event/<int:id>/edit/', views.event_edit, name='editevent'),
    path('event/<int:id>/delete/', views.event_delete, name='deleteevent'),

    path('venues/', views.venue_all, name='venues'),
    path('venues/txt/', views.venuestxt, name='venuestxt'),
    path('venues/csv/', views.venuescsv, name='venuescsv'),
    path('venues/pdf/', views.venuespdf, name='venuespdf'),
    path('venue/add/', views.venue_add, name='venue-add'),
    path('venue/<int:id>/', views.indvenue, name='indvenue'),
    path('venue/<int:id>/edit/', views.venue_edit, name='editvenue'),
    path('venue/<int:id>/delete/', views.venue_delete, name='deletevenue'),

]