import email

from django.db import models
from django.contrib.auth.models import User
from rest_framework import status


class Customer(models.Model):
    user=models.OneToOneField(User,null=True,blank=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=50,blank=True)
    email= models.EmailField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField()
    digital=models.BooleanField(default=False)

    def  __str__(self):
        return self.name


class Order(models.Model):
    customer=models.ForeignKey('store.Customer',on_delete=models.CASCADE,null=True,blank=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False)
    transaction_id=models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey('store.Product', on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey('store.Order', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey('store.Customer', on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey('store.Order', on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


