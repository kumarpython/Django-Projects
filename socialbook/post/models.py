from django.contrib.auth.models import User
from django.db import models
from django.db.models.functions import datetime
from django.urls import reverse


class Post(models.Model):
    # author=models.CharField(max_length=50)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(max_length=100)
    on=models.DateTimeField(auto_now_add=True)
    url=models.URLField(null=True,blank=True)
    approved=models.BooleanField(default=True)
    image=models.ImageField(upload_to='post_image',blank=True)

    @property
    def till(self):
        till=datetime.now() - self.on
        return till

    def get_absolute_url(self) :
        return reverse('detail', kwargs={'pk' : self.pk})


class UserGroup(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=200)
    image=models.ImageField(upload_to='group_pic')
    post=models.ForeignKey('post.Post',on_delete=models.CASCADE)
    category=models.CharField(max_length=20,default=1)
    # members=models.ForeignKey('profiles.Profile',on_delete=models.CASCADE)

    def __str__(self):
        return f'Group {self.name}'