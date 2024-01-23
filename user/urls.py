from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user.views.templates import user_home, signup, logoutView, MyLoginView
from user.views.api import CreateUserApi, LoginApi, LogoutApi
# ,LoginUserView

urlpatterns = [
    path('', user_home, name='user-home'),
    path('signup/', signup, name='signup'),
    path('logout-view/', logoutView, name='logout-view'),
    path('login-view/', MyLoginView.as_view(), name='login-view'),
    path('create-user-api/', CreateUserApi.as_view(), name='create-user-api'),
    path('login-api/', LoginApi.as_view(), name='login-api'),
    path('logout-api/', LogoutApi.as_view(), name='logout-api'),
    path('api-token/', obtain_auth_token, name='api-token'),
]
