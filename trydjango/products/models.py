from django.db import models


class Product(models.Model):
    title=          models.CharField(max_length=100)
    description=    models.TextField(blank=True,null=True)
    price=          models.DecimalField(max_digits=10,decimal_places=2)
    summary=          models.TextField(blank=True,null=True)
    featured=          models.BooleanField(null=True,default=True)

    def get_absolute_url(self):
         return reverse('products:detail',kwargs={'id':self.id}) # return f'product/{self.id}/'