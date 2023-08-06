from django.contrib import admin
from inventory.models import Category, Supplier, ImagesUpload, Product, Inventory, Customer, Order, Transaction, Location, OnlineBuyer, Shipments, Employees

# Register your models here.
# class ProductAdmin(admin.StackedInline):
#     model = Product

# class ImageAdmin(admin.ModelAdmin):
#     inlines = [ProductAdmin]

admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(ImagesUpload)
admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Transaction)
admin.site.register(Location)
admin.site.register(OnlineBuyer)
admin.site.register(Shipments)
admin.site.register(Employees)