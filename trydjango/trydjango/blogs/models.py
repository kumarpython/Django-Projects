from django.db import models
from django.urls import reverse


class Article(models.Model):
    title=models.CharField(max_length=120)
    content=models.TextField()
    active=models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("blogs:blogs-detail",kwargs={'id':self.id})