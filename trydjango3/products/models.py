from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    summary = models.TextField()