from django.db import models
from django.urls import reverse


class Category(models.Model):

    category =      models.CharField(max_length=200)
    category_summary =       models.CharField(max_length=200)
    category_slug =          models.TextField(default=0)

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('ss', kwargs={'ss': self.ss})


class Series(models.Model):
    series =        models.CharField(max_length=100)
    series_category =      models.ForeignKey(Category, default=0,on_delete=models.SET_DEFAULT)
    series_summary =       models.TextField()

    def __str__(self):
        return self.series

    def get_absolute_url(self):
        return reverse('ss', kwargs={'ss': self.ss})


class Tutorial(models.Model):
    title =         models.CharField(max_length=50)
    content =       models.TextField()
    published =     models.DateTimeField(auto_now_add=True)
    # https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.ForeignKey.on_delete
    tseries = models.ForeignKey(Series, default=0, on_delete=models.SET_DEFAULT)
    tslug = models.CharField(max_length=100, default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ss', kwargs={'pk': self.ss})