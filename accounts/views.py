from rest_framework import permissions, generics

from .serializers import UserSerializer


class CreateUserAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
