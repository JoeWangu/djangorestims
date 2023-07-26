from django.urls import path, include
from rest_framework import routers
# from rest_framework.authtoken.views import obtain_auth_token
from inventory.views.api import ProductViewSet,LocationViewSet,FamilyViewSet,TransactionViewSet  

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, 'products')
router.register(r'location', LocationViewSet, 'location')
router.register(r'family', FamilyViewSet, 'family')
router.register(r'transaction', TransactionViewSet, 'transaction')

urlpatterns = [
    # path('', obtain_auth_token, name='api_token_auth'),
    path('api/', include(router.urls)),
]
