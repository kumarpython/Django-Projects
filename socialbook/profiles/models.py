from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from django.urls import reverse


class UserProfile(models.Model):
    GENDERCHOICES = [('M','Male'),('F', 'Female')]
    MARRAIGECHOICES = [('Y','Yes'),('N', 'No')]
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    friends=models.ManyToManyField(User,related_name='Friends',blank=True)
    fname=models.CharField(max_length=50,help_text='First Name')
    lname=models.CharField(max_length=50,help_text='Last Name')
    gender = models.CharField(choices=GENDERCHOICES,max_length=10)
    email=models.EmailField()
    mobile= models.IntegerField()
    dob=models.DateField(help_text='Date of Birth')
    married=models.CharField(choices=MARRAIGECHOICES,max_length=10)
    pic=models.ImageField(upload_to='profile_pic')
    country = models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    zipcode=models.IntegerField()
    ip=models.GenericIPAddressField()
    mac=models.CharField(max_length=10)

    # @property
    # def age(self):
    #     age=datetime.today() - self.dob.date()
    #     return age

    def __str__(self):
        return f'{self.fname}  {self.lname}'

    def resize(self,*args,**kwargs):
        img = Image.open(self.pic)
        img.thumbnail((200, 200))
        super().save(*args, **kwargs)

    def get_absolute_url(self) :
        return reverse('profile', kwargs={'pk' : self.pk})


class Friendship(models.Model):
    receiver=models.ForeignKey(User,related_name='Receiver',on_delete=models.CASCADE)
    sender=models.ForeignKey(User,related_name='Sender',on_delete=models.CASCADE)
    accepted=models.BooleanField()
    on=models.DateTimeField(auto_now=True)

