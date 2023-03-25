from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Category(models.Model):
    class Meta:
        verbose_name = "カテゴリー"
        verbose_name_plural = "カテゴリー"

    id = models.UUIDField("ID", default=uuid4, primary_key=True, editable=False)
    name = models.CharField("カテゴリー名", max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Meta:
        verbose_name = "タスク"
        verbose_name_plural = "タスク"
        ordering = ["-created_at"]

    class Status(models.IntegerChoices):
        NOT_STARTED = 0, _("新規")
        ON_GOING = 1, _("作業中")
        COMPLETED = 2, _("完了")

    id = models.UUIDField("ID", default=uuid4, primary_key=True, editable=False)
    title = models.CharField("タイトル", max_length=100)
    description = models.CharField("説明", max_length=300)
    status = models.IntegerField(
        "ステータス", choices=Status.choices, default=Status.NOT_STARTED
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="カテゴリー"
    )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="task_owner", verbose_name="タスク作成者"
    )
    started_at = models.DateTimeField("タスク開始時間", null=True, blank=True)
    paused_at = models.DateTimeField("タスク一時停止時間", null=True, blank=True)
    total_time = models.DurationField("合計作業時間", default=0, null=True, blank=True)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)

    def __str__(self):
        return self.title
