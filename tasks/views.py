from rest_framework import filters, permissions, viewsets

from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer


class OwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner.id == request.user.id


class CategoryViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post", "head", "options"]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TaskViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post", "put", "delete", "head", "options"]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated, OwnerPermission)
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "description", "owner__username"]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
