from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    user_type_choices={(1,'Admin'),(2,'Staff'),(3,'Merchant'),(4,'Customer')}
    user_type=models.CharField(max_length=50,choices=user_type_choices,default=4)


class AdminUser(models.Model):
    name= models.CharField(max_length=50)
    profile_pics=models.ImageField(default='', upload_to='admin_profile_pics')
    created_at=models.DateTimeField(auto_now_add=True)


class StaffUser(models.Model):
    name = models.CharField(max_length=50)
    profile_pics=models.ImageField(default='', upload_to='staff_profile_pics')
    created_at=models.DateTimeField(auto_now_add=True)


class MerchantUser(models.Model):
    name = models.CharField(max_length=50)
    profile_pics=models.ImageField(default='', upload_to='merchant_profile_pics')
    company_name=models.CharField(max_length=50)
    gst_details=models.CharField(max_length=50)
    address=models.TextField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)


class CustomerUser(models.Model):
    profile_pics=models.ImageField(default='', upload_to='customer_profile_pics')
    created_at=models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name= models.CharField(max_length=50)
    slug=models.SlugField(default=True)
    thumbnail=models.ImageField(default='', upload_to='category_thumbnail')
    description=models.TextField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)


class SubCategory(models.Model) :
    name = models.CharField(max_length=50)
    parent=models.ForeignKey('ecommerceapp.category',on_delete=models.CASCADE)
    slug = models.SlugField(default=True)
    thumbnail = models.ImageField(default='', upload_to='subcategory_thumbnail')
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name= models.CharField(max_length=50)
    category=models.ForeignKey('ecommerceapp.Category',null=True,on_delete=models.SET_NULL)
    subcategory=models.ForeignKey('ecommerceapp.SubCategory',on_delete=models.SET_NULL)
    brand=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    disc_price=models.DecimalField(max_digits=5,decimal_places=2)
    image=models.ImageField(default='',upload_to='products')
    desc=models.TextField(max_length=200)
    seller=models.ManyToManyField('ecommerceapp.MerchantUser',null=True,on_delete=models.SET_NULL)
    added_by=models.ForeignKey('ecommerceapp.MerchantUser',null=True,on_delete=models.SET_NULL)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active= models.BooleanField(default=False)
    is_featured= models.BooleanField(default=False)