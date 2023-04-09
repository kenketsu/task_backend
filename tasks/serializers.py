from rest_framework import serializers

from .models import Category, Task


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class TaskSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source="category.name")  # カテゴリー名の文字列
    owner_username = serializers.ReadOnlyField(source="owner.username")  # タスクのオーナー名の文字列
    status_name = serializers.CharField(
        source="get_status_display", read_only=True
    )  # ステータスの文字列
    progress_item = serializers.CharField(
        source="get_progress_display", read_only=True
    )  # 進捗の文字列
    created_at = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M", read_only=True
    )  # 作成日時のフォーマット
    total_time_formatted = serializers.SerializerMethodField()

    def get_total_time_formatted(self, obj):
        total_time_in_milliseconds = obj.total_time or 0
        total_time_in_seconds = total_time_in_milliseconds // 1000
        hours = total_time_in_seconds // 3600
        minutes = (total_time_in_seconds % 3600) // 60
        seconds = total_time_in_seconds % 60
        return f"{hours}:{minutes:02d}:{seconds:02d}"

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
            "progress",
            "progress_item",
            "started_at",
            "total_time",
            "total_time_formatted",
            "owner",
            "owner_username",
            "created_at",
        ]
        extra_kwargs = {"owner": {"read_only": True}}
