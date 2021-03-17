from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
        return reverse('users:profile',kwargs={'username':self.username})


    def save(self):
        super().save()

        img=Image.open(self.image.path)
        if img.height>200 or img.width>200:
            img.thumbnail((200,200))
            img.save(self.image.path)
