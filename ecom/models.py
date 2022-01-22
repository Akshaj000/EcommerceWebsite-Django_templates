from contextlib import nullcontext
from statistics import mode
from unicodedata import category
from django.db import models
from django.conf import settings
from decimal import Decimal
from payments import PurchasedItem
from payments.models import BasePayment

# Create your models here.

class Customer(models.Model):
    photo = models.ImageField(upload_to=settings.MEDIA_ROOT,blank=True)
    name = models.CharField(max_length=200, null=True,unique=True)
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
    cart = models.ManyToManyField(Cart)
    payment_status = models.BooleanField(null=True)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200,null=True,choices=STATUS)

    def __str__(self):
        try:
            return str(self.cart.product.name)+"_"+str(self.cart.customer.name)
        except:
            return "Unknown"

class Payment(BasePayment):

    def get_failure_url(self):
        return 'home'

    def get_success_url(self):
        return 'cart'

    def get_purchased_items(self):
        yield PurchasedItem(name='The Hound of the Baskervilles', sku='BSKV',quantity=9, price=Decimal(10), currency='USD')