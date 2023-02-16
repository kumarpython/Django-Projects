from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Venue(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=50,blank=True)
    web = models.URLField(blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self) :
    #     return reverse('indvenue', kwargs={'pk' : self.pk})


class MyClubMember(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50,blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.fname + " " + self.lname


class Events(models.Model):
    name = models.CharField(max_length=50)
    event_date = models.DateTimeField()
    venue = models.ForeignKey(Venue, null=True, blank=True, on_delete=models.SET_NULL)
    manager = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubMember, blank=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self) :
    #     return reverse('indevent', kwargs={'pk' : self.pk})
