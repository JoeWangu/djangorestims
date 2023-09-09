# from django.contrib.auth import authenticate
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from user.models import User
from user.serializers import UserSerializer, LoginSerializer
from rest_framework import views
# from django.contrib.auth import login
# from django.contrib.auth import logout
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator


class CreateUserApi(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 201:
            user = User.objects.get(username=request.data['username'])
            token = Token.objects.create(user=user)
            data = {'user': response.data, 'token': str(token)}
            return Response(data, status=status.HTTP_201_CREATED)
        return response

#  TOKEN BASED VIEWS
# @api_view(['POST'])
# @csrf_exempt
# @method_decorator(csrf_exempt, name='dispatch')
class LoginApi(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data, context={ 'request': self.request }) # type: ignore
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user'] # type: ignore
        # token = Token.objects.get_or_create(user = user)
        token, created = Token.objects.get_or_create(user=user)
        data = {'user': request.data['username'], 'token': token.key, 'created': created}
        # login(request, user)
        return Response(data, status=status.HTTP_202_ACCEPTED)

# @api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class LogoutApi(views.APIView):
    def post(self, request, format=None):
        # Get the token associated with the current user and delete it
        try:
            request.user.auth_token.delete()
        except (AttributeError, Token.DoesNotExist):
            # The user didn't have a token or the token doesn't exist
            pass

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    # SESSION BASED VIEWS
# class LoginApi(views.APIView):
#     # This view should be accessible also for unauthenticated users.
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         serializer = LoginSerializer(data=self.request.data, context={ 'request': self.request }) # type: ignore
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user'] # type: ignore
#         login(request, user)
#         return Response(None, status=status.HTTP_202_ACCEPTED)

# class LogoutApi(views.APIView):
#     def post(self, request, format=None):
#         logout(request)
#         return Response(None, status=status.HTTP_204_NO_CONTENT)


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
