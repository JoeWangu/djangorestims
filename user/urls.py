from django.urls import path
from user.views.templates import user_home, signup, logoutView, MyLoginView
from user.views.api import CreateUserView, LoginView, LogoutUserView
                            #,LoginUserView

urlpatterns = [
    path('', user_home, name='user_home'),
    path('signup/', signup, name='signup'),
    path('logoutView/', logoutView, name='logoutView'),
    path('MyLoginView/', MyLoginView.as_view(), name='MyLoginView'),
    path('CreateUserView/', CreateUserView.as_view(), name='CreateUserView'),
    path('LoginView/', LoginView.as_view(), name='LoginView'),
    path('LogoutUserView/', LogoutUserView.as_view(), name='LogoutUserView'),
    # path('LoginUserView/', LoginUserView.as_view(), name='LoginUserView'),
]
