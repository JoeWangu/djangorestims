from rest_framework import serializers
from inventory.models import Category, Supplier, ImagesUpload, Product, Inventory, Customer, Order, Transaction, Location, OnlineBuyer, Shipments, Employees

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class ImagesUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesUpload
        fields = '__all__'

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())
    image = serializers.PrimaryKeyRelatedField(queryset=ImagesUpload.objects.all())
    
    class Meta:
        model = Product
        fields = ['name', 'model_number', 'specifications', 'price', 'image', 'category', 'supplier']

class InventorySerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    
    class Meta:
        model = Inventory
        fields = ['product', 'last_sales_date', 'quantity_sold', 'sales', 'stock_date', 'quantity_in_stock', 'minimum_quantity']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Order
        fields = ['order_date', 'delivery_date', 'status', 'customer', 'product']

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    
    class Meta:
        model = Transaction
        fields = ['transaction_type','transaction_date','product','quantity']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class OnlineBuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineBuyer
        fields = '__all__'

class ShipmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipments
        fields = '__all__'

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'