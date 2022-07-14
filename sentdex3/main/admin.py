from django.contrib import admin
from .models import Tutorial,Category,Series
from tinymce.widgets import TinyMCE
from django.db import models

formfield_overrides = {models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},}

admin.site.register(Tutorial)
admin.site.register(Category)
admin.site.register(Series)
