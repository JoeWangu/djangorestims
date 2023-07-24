from django.contrib import admin
from .models import Location, Family, Product, Transaction

# Register your models here.
admin.site.register(Location)
admin.site.register(Family)
admin.site.register(Product)
admin.site.register(Transaction)