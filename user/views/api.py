# from django.contrib.auth import authenticate
from rest_framework import generics, permissions, status
# from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from user.models import User
from user.serializers import UserSerializer, LoginSerializer
from rest_framework import views
from django.contrib.auth import login
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data, context={ 'request': self.request }) # type: ignore
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user'] # type: ignore
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)

class LogoutUserView(views.APIView):
    def post(self, request, format=None):
        logout(request)
        return Response(None, status=status.HTTP_204_NO_CONTENT)


# class LogoutUserView(generics.GenericAPIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         request.auth.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class LoginUserView(generics.GenericAPIView):
#     permission_classes = (permissions.AllowAny,)
#     serializer_class = UserSerializer

#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key})
#         else:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
