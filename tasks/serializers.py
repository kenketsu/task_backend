from rest_framework import serializers

from .models import Category, Task


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class TaskSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source="category.name")
    owner_username = serializers.ReadOnlyField(source="owner.username")
    status_name = serializers.CharField(source="get_status_display", read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    total_time = serializers.DurationField(format="%H:%M:%S")

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "status",
            "status_name",
            "category",
            "category_name",
            "owner",
            "owner_username",
            "started_at",
            "paused_at",
            "created_at",
            "total_time",
        ]
        extra_kwargs = {"owner": {"read_only": True}}
