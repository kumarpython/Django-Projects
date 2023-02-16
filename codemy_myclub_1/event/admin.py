from django.contrib import admin
from .models import Events,Venue,MyClubMember
# admin.site.register(Events)
# admin.site.register(Venue)
admin.site.register(MyClubMember)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name' , 'phone' , 'email')
    ordering = ['name']
    search_fields = ['name']


@admin.register(Events)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name' , 'event_date' , 'venue' , 'manager')
    list_filter = ['venue' , 'manager']
    ordering = ['event_date']
    search_fields = ['name']