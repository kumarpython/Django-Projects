from django.db import models
from django.urls import reverse


class Article(models.Model):
    title =         models.CharField(null=True,blank=True,max_length=25)
    content =       models.TextField(null=True,blank=True)
    active =        models.BooleanField(null=True,blank=True,default=True)

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.id})