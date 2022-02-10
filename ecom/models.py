from contextlib import nullcontext
from statistics import mode
from unicodedata import category
from django.db import models
from django.conf import settings
from decimal import Decimal


# Create your models here.

class Customer(models.Model):
    photo = models.ImageField(upload_to=settings.MEDIA_ROOT,blank=True)
    name = models.CharField(max_length=200, null=True,unique=True)
    actname = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    district = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=350, null=True)
    postalcode = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True) 
    
    def __str__(self):
        return self.name

class Category(models.Model):
    categoryname  = models.CharField(max_length=200,null=True,unique=True)
    def __str__(self):
        return self.categoryname


class Product(models.Model):
    name  = models.CharField(max_length=200,null=True,unique=True)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT)
    description = models.TextField(null=True)
    price = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    category = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.name

class Cart(models.Model):
    name = models.CharField(max_length=200, null=True,unique=True)
    product = models.ForeignKey(Product, null=True , on_delete= models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True , on_delete= models.SET_NULL)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    count  = models.IntegerField()
    
    def totalprice(self):
        return self.product.price*self.count


    def __str__(self):
        try:
            return str(self.product.name)+"_"+str(self.customer.name)
        except:
            return "Unknown"
    


class Order(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered')
        )
    name = models.CharField(max_length=200, null=True)
    product = models.ForeignKey(Product, null=True , on_delete= models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True , on_delete= models.SET_NULL)
    totalprice = models.FloatField(null=True)
    count  = models.IntegerField(null=True)
    payment_status = models.BooleanField(null=True)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200,null=True,choices=STATUS)

    def __str__(self):
        try:
            return str(self.name)
        except:
            return "Unknown"


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        
    for user in User.objects.all():
        Token.objects.get_or_create(user=user)
