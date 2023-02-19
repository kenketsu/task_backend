from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from .serializers import UserSerializer

User = get_user_model()


class CreateUserAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
