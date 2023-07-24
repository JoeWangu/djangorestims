# from django.urls import path
# # from .views import dashboard, family_list
# from django.urls import re_path

# from inventory import views

# urlpatterns = [
#     path('', views.dashboard, name='dashboard'),
#     re_path(r'^products/$', views.product_list),
#     re_path(r'^products/(?P<pk>[0-9]+)$', views.product_detail),
#     re_path(r'^families/$', views.family_list.as_view()),
#     re_path(r'^families/(?P<pk>[0-9]+)$', views.family_detail.as_view()),
#     re_path(r'^locations/$', views.location_list.as_view()),
#     re_path(r'^locations/(?P<pk>[0-9]+)$', views.location_detail.as_view()),
#     re_path(r'^transactions/$', views.transaction_list.as_view()),
#     re_path(r'^transactions/(?P<pk>[0-9]+)$', views.transaction_detail.as_view()),
# ]

# urls.py

from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet,LocationViewSet,FamilyViewSet,TransactionViewSet  

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'products', LocationViewSet)
router.register(r'products', FamilyViewSet)
router.register(r'products', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
