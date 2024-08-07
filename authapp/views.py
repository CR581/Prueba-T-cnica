from rest_framework import generics
from .serializers import UserSerializer, UserSignupSerializer, UserLoginSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        cc = serializer.validated_data['cc']
        user = authenticate(email=email, password=cc)  
        if user is not None:
            login(request, user)
            return Response({'message': 'Sesión iniciada correctamente'}, status=status.HTTP_200_OK)
        return Response({'non_field_errors': ['Correo o Número de documento incorrecto']}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': 'Sesión iniciada correctamente'}, status=status.HTTP_200_OK)
    
    
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
