from rest_framework import serializers
from .models import Location, Family, Product, Transaction

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location 
        fields = ['reference','title', 'description']

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family 
        fields = ['reference','title', 'description','unit','minQuantity']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product 
        fields = ['sku','barcode', 'title', 'description','unitCost','unit','quantity','minQuantity','location','family']

class TransactionSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Transaction 
        fields = ['sku','barcode','comment','unitCost','quantity','product','date','reason']