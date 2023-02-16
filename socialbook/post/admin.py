from django.contrib import admin
from .models import Post,UserGroup


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author','on','approved']
    list_filter = ["author",'approved']
    ordering = ['-on']
    search_fields = ['author','on']

    class Meta:
        verbose_name_plural='Posts'


@admin.register(UserGroup)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name','post','category']
    list_filter = ["category"]
    search_fields = ['name']

