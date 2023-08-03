from django.urls import path, include
from rest_framework import routers
# from rest_framework.authtoken.views import obtain_auth_token
from inventory.views.api import CategoryViewSet, SupplierViewSet, ImagesUploadViewSet, ProductViewSet, InventoryViewSet, CustomerViewSet, OrderViewSet, TransactionViewSet, LocationViewSet, OnlineBuyerViewSet, ShipmentsViewSet, EmployeesViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet, 'category')
router.register(r'supplier', SupplierViewSet, 'supplier')
router.register(r'images', ImagesUploadViewSet, 'images')
router.register(r'products', ProductViewSet, 'products')
router.register(r'inventory', InventoryViewSet, 'inventory')
router.register(r'customer', CustomerViewSet, 'customer')
router.register(r'order', OrderViewSet, 'order')
router.register(r'transaction', TransactionViewSet, 'transaction')
router.register(r'location', LocationViewSet, 'location')
router.register(r'onlinebuyer', OnlineBuyerViewSet, 'onlinebuyer')
router.register(r'shipments', ShipmentsViewSet, 'shipments')
router.register(r'employees', EmployeesViewSet, 'employees')

urlpatterns = [
    # path('', obtain_auth_token, name='api_token_auth'),
    path('api/', include(router.urls)),
]
