from rest_framework import serializers
from .models import Location, Family, Product, Transaction

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location 
        fields = '__all__'

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family 
        fields = '__all__'

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all())
    family = serializers.PrimaryKeyRelatedField(queryset=Family.objects.all())
    class Meta:
        model = Product 
        fields = ['sku','barcode', 'title', 'description','unitCost','unit','quantity','minQuantity','location','family']

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    # product = ProductSerializer(read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    class Meta:
        model = Transaction 
        fields = ['sku','barcode','comment','unitCost','quantity','product','date','reason']

