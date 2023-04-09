from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets

from .models import Profile
from .serializers import ProfileSerializer, UserSerializer

User = get_user_model()


class CreateUserAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


class LoginUserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_names = ["get", "post", "put", "head", "options"]

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)
