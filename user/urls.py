from django.urls import path
from .views import user_home, signup, logoutView, MyLoginView

urlpatterns = [
    path('', user_home, name='user_home'),
    path('signup/', signup, name='signup'),
    path('logoutView/', logoutView, name='logoutView'),
    path('MyLoginView/', MyLoginView.as_view(), name='MyLoginView'),
]
