from django.contrib import admin

from .models import Event , Member , Venue

#admin.site.register(Event)
admin.site.register(Member)


# admin.site.register(Venue)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin) :
	list_display = ('name' , 'phone' , 'email')
	ordering = ['name']
	search_fields = ['name']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin) :
	list_display = ('name' , 'date' , 'venue' , 'manager')
	list_filter = ['date' , 'venue' , 'manager']
	ordering = ['date']
	search_fields = ['name']
