from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from datetime import date


class Event(models.Model) :
    name = models.CharField(max_length=50)
    date = models.DateTimeField()
    venue = models.ForeignKey('events.Venue', blank=True, null=True, on_delete=models.SET_NULL)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    desc = models.TextField(blank=True)
    attendees = models.ManyToManyField('events.Member')
    img=models.ImageField(null=True,blank=True,upload_to='events')
    approved=models.BooleanField(default=False)

    def __str__(self) :
        return self.name

    def get_absolute_url(self) :
        return reverse('indevent', kwargs={'pk' : self.pk})

    @property
    def till(self):
        return self.date.date() - date.today()


class Venue(models.Model) :
    name = models.CharField(max_length=50)
    address = models.TextField()
    zipcode = models.IntegerField()
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    web = models.URLField(blank=True)
    owner=models.ForeignKey(User, blank=False, default=1,on_delete=models.SET_DEFAULT)
    img=models.ImageField(null=True,blank=True,upload_to='venues')

    def __str__(self) :
        return self.name

    def get_absolute_url(self) :
        return reverse('indvenue', kwargs={'pk' : self.pk})


class Member(models.Model) :
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self) :
        return self.fname + ' ' + self.lname
