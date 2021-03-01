from django.db import models
from django.urls import reverse


class Product(models.Model):
    title=          models.CharField(max_length=100)
    description =   models.TextField(blank=True,null=True)
    price=          models.DecimalField(decimal_places=2,max_digits=10)
    summary=        models.TextField(blank=False)
    featured=       models.BooleanField(null=True,default=False)

    def get_absolute_url(self):
        return reverse("products:products-detail",kwargs={'id':self.id})
        # return f"/products/{self.id}/"