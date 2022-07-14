from django.db import models
from django.urls import reverse


class Product(models.Model):
    title =         models.CharField(max_length=20)
    description =   models.TextField(blank=True,null=True)
    price =         models.DecimalField(max_digits=5,decimal_places=2)
    summary =       models.TextField(blank=True,null=True)
    featured =      models.BooleanField(default=False)

    def get_url(self):
        return reverse('products : detail',kwargs={'ID':self.id})