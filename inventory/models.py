from __future__ import unicode_literals
from typing import Iterable, Optional
# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
import os
from PIL import Image

DC = 'DC'
NY = 'NewYork'
TX = 'Texas'

LOCATION_CHOICES = [
    (DC, 'Washington, D.C.'),
    (NY, 'New York City'),
    (TX, 'Austin'),
]

TRANSACTION_TYPES = [
        ('IN', 'Incoming'),
        ('OUT', 'Outgoing'),
        ('TRANSFER', 'Transfer'),
]

STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
        ('bulk', 'Bulk'),
)

# images = os.path.join(settings.MEDIA_ROOT, 'images')
# IMAGE_CHOICES = [(filename, filename) for filename in os.listdir(images)]
def get_default_image():
    # Get or create the default image object
    default_image = ImagesUpload.objects.get_or_create(image='images/default.jpg')
    return default_image[0]
# default_image = images + '/default.jpg'

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank= True, default='not provided')

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ImagesUpload(models.Model):
    image = models.ImageField(upload_to='images/',max_length=255, null=True, blank=True)

    def __str__(self):
        return self.image.name
    # resizing the image, you can change parameters like size and quality.
    def save(self, *args, **kwargs):
        super(ImagesUpload, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path, quality=100, optimize=True)
        return super().save()

class Product(models.Model):
    name = models.CharField(max_length=255)
    model_number = models.CharField(max_length=255)
    specifications = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # image = models.ImageField(max_length=100, choices=IMAGE_CHOICES, null=True, blank=True, default='default.jpg')
    image = models.ForeignKey(ImagesUpload, on_delete=models.SET_DEFAULT, default=get_default_image, max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    last_sales_date = models.DateField(auto_now=True)
    quantity_sold = models.IntegerField(null=False,blank=False)
    sales = models.DecimalField(max_digits=19,decimal_places=2,null=False,blank=False)
    stock_date = models.DateField(auto_now_add=True)
    quantity_in_stock = models.IntegerField()
    minimum_quantity = models.IntegerField()

class Customer(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=255)
    address = models.CharField(max_length=200)
    extra_info = models.TextField(null=True, blank=True, default='none')

    def __str__(self):
        return self.name

class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Order #{self.id}" # type: ignore

# track the movement of inventory, such as when items are received from suppliers, sold to customers, or transferred between locations. 
class Transaction(models.Model):
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPES)
    transaction_date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return 'Transaction :  %d' % (self.id)# type: ignore

class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(choices=LOCATION_CHOICES, default=DC,max_length=255)
    capacity = models.IntegerField(null=True, blank=True)
    contact_information = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class OnlineBuyer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Shipments(models.Model):
    shipment_date = models.DateTimeField()
    tracking_number = models.IntegerField()
    recipient_information = models.CharField(max_length=255)

class Employees(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    contact_info = models.CharField(max_length=255, null=True, blank=True)