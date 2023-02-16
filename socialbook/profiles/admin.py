from django.contrib import admin
from .models import UserProfile,Friendship


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['fname','lname','email','mobile','dob','married','pic','country','state','city','ip','mac']
    list_filter = ['gender','country']
    ordering = ['dob']
    search_fields = ['fname','lname','email','city']

    class Meta:
        verbose_name_plural='UserProfiles'


admin.site.register(Friendship)