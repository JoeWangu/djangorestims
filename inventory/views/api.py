from rest_framework import viewsets
# from rest_framework.authentication import SessionAuthentication, TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from inventory.models import Category, Supplier, ImagesUpload, Product, Inventory, Customer, Order, Transaction, Location, OnlineBuyer, Shipments, Employees
from inventory.serializers import CategorySerializer, SupplierSerializer, ImagesUploadSerializer, ProductSerializer, InventorySerializer, CustomerSerializer, OrderSerializer, TransactionSerializer, LocationSerializer, OnlineBuyerSerializer, ShipmentsSerializer, EmployeesSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    # authentication_classes = [SessionAuthentication, TokenAuthentication]
    # permission_classes = [IsAuthenticated]

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all().order_by('name')
    serializer_class = SupplierSerializer

class ImagesUploadViewSet(viewsets.ModelViewSet):
    queryset = ImagesUpload.objects.all().order_by('id')
    serializer_class = ImagesUploadSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all().order_by('product')
    serializer_class = InventorySerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('name')
    serializer_class = CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('order_date')
    serializer_class = OrderSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('transaction_date')
    serializer_class = TransactionSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('name')
    serializer_class = LocationSerializer

class OnlineBuyerViewSet(viewsets.ModelViewSet):
    queryset = OnlineBuyer.objects.all().order_by('name')
    serializer_class = OnlineBuyerSerializer

class ShipmentsViewSet(viewsets.ModelViewSet):
    queryset = Shipments.objects.all().order_by('tracking_number')
    serializer_class = ShipmentsSerializer

class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all().order_by('name')
    serializer_class = EmployeesSerializer