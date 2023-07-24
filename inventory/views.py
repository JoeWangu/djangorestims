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
# @login_required
# def dashboard(request):
#     title = 'Dashboard'
#     context = {
#         'title': title,
#     }
#     return render(request, 'rest/dashboard.html', context)

# # products
# @api_view(['GET', 'POST'])
# def product_list(request):
#     """
#     List all products, or create a new product.
#     """
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ProductSerializer(products,context={'request': request} ,many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def product_detail(request, pk):
#     """
#     Retrieve, update or delete a product instance.
#     """
#     try:
#         product = Product.objects.get(pk=pk)
#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ProductSerializer(product,context={'request': request})
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ProductSerializer(product, data=request.data,context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# # class family_list(generics.ListCreateAPIView):
# #     queryset = Family.objects.all()
# #     serializer_class = FamilySerializer

# class family_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Family.objects.all()
#     serializer_class = FamilySerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# # class family_detail(generics.RetrieveUpdateDestroyAPIView):
# #     queryset = Family.objects.all()
# #     serializer_class = FamilySerializer

# class family_detail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):

#     queryset = Family.objects.all()
#     serializer_class = FamilySerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs) 

# class location_list(generics.ListCreateAPIView):
#     queryset = Location.objects.all()
#     serializer_class = LocationSerializer

# class location_detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Location.objects.all()
#     serializer_class =  LocationSerializer

# class transaction_list(generics.ListCreateAPIView):
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer

# class transaction_detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Transaction.objects.all()
#     serializer_class =  TransactionSerializer

from rest_framework import viewsets
from .models import Product, Location ,Family ,Transaction 
from .serializers import ProductSerializer, TransactionSerializer, FamilySerializer, LocationSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


# views.py

# from rest_framework import permissions
# from rest_framework.response import Response
# from rest_framework.views import APIView

# class MyView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)
