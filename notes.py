# ######################################### SERIALIZER NOTES ###########################################################
# The serializer is used to convert the data into a format that can be sent over the network.
#examples from serializer.py in inventory

# to include all fields at once
class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'

# to exclude some fields
class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family 
        exclude = 'minQuantity'

# in class ProductSerializer....As you can see we have included the related models location and family .In this case ModelSerializer takes the primary keys by default so you'll get something like this, depending on data you have in your database. ..."location": 1,...
# What if you want to get the whole related objects ?
# You can use the depth option in Meta class eg.
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ('sku','barcode', 'title', 'description','location','family')
        depth = 1
# you will get something like this,
{
        "sku": "Product001",
        "barcode": "xxxxxxxxx",
        "title": "Product 001",
        "description": "product 001",
        "location": {
            "id": 1,
            "reference": "LOC001",
            "title": "Location 001",
            "description": "Location 001"
        },
# Or you can specify the fields explicitly .
# class ProductSerializer(serializers.ModelSerializer):

    location = LocationSerializer()
    family = FamilySerializer()
    class Meta:
        model = Product 
        fields = ('sku','barcode', 'title', 'description','location','family')

# Using ModelSerializer ,the default way to serialize a relationship field is primary keys but we have also other representations such as :
# 1.Hyperlinks - uses hyperlinks instead of primary keys to represent relationships .
# 2.Complete nested instances ,
# 3.Custom representation

# ######################################### VIEWS NOTES ###########################################################

# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# # -*- coding: utf-8 -*-
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status , generics , mixins
# from .models import Product, Location ,Family ,Transaction 
# from .serializers import ProductSerializer, TransactionSerializer, FamilySerializer, LocationSerializer

# # Create your views here.
@login_required
def dashboard(request):
    title = 'Dashboard'
    context = {
        'title': title,
    }
    return render(request, 'rest/dashboard.html', context)

# # products
@api_view(['GET', 'POST'])
def product_list(request):
    """
    List all products, or create a new product.
    """
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products,context={'request': request} ,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    """
    Retrieve, update or delete a product instance.
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class family_list(generics.ListCreateAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class family_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class family_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

class family_detail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):

    queryset = Family.objects.all()
    serializer_class = FamilySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) 

class location_list(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class location_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class =  LocationSerializer

class transaction_list(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class transaction_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class =  TransactionSerializer




# views.py

# from rest_framework import permissions
# from rest_framework.response import Response
# from rest_framework.views import APIView

class MyView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


# ######################################### URLS NOTES ###########################################################

# from django.urls import path
# # from .views import dashboard, family_list
# from django.urls import re_path

# from inventory import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    re_path(r'^products/$', views.product_list),
    re_path(r'^products/(?P<pk>[0-9]+)$', views.product_detail),
    re_path(r'^families/$', views.family_list.as_view()),
    re_path(r'^families/(?P<pk>[0-9]+)$', views.family_detail.as_view()),
    re_path(r'^locations/$', views.location_list.as_view()),
    re_path(r'^locations/(?P<pk>[0-9]+)$', views.location_detail.as_view()),
    re_path(r'^transactions/$', views.transaction_list.as_view()),
    re_path(r'^transactions/(?P<pk>[0-9]+)$', views.transaction_detail.as_view()),
]

# urls.py

########################################## MORE SERIALIZER NOTES ###########################################################

###HANDLING NESTED UPDATING
class ProductSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    family = FamilySerializer()

    class Meta:
        model = Product
        fields = '__all__'

    def update(self, instance, validated_data):
        location_data = validated_data.pop('location', None)
        if location_data:
            location_serializer = LocationSerializer(instance.location, data=location_data)
            location_serializer.is_valid(raise_exception=True)
            location_serializer.save()

        family_data = validated_data.pop('family', None)
        if family_data:
            family_serializer = FamilySerializer(instance.family, data=family_data)
            family_serializer.is_valid(raise_exception=True)
            family_serializer.save()

        return super().update(instance, validated_data)
