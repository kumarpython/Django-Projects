from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Article(models.Model):
    title=      models.CharField(max_length=120)
    content=    models.TextField()
    author=     models.ForeignKey(User,on_delete=models.CASCADE)
    published=  models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
         return reverse('blog:article-detail',kwargs={'pk':self.pk}) # return f'product/{self.id}/'