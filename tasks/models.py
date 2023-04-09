from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Category(models.Model):
    class Meta:
        verbose_name = "カテゴリー"
        verbose_name_plural = "カテゴリー"

    name = models.CharField("カテゴリー名", max_length=100, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Meta:
        verbose_name = "タスク"
        verbose_name_plural = "タスク"
        ordering = ["-created_at"]

    class Status(models.IntegerChoices):
        NOT_STARTED = 1, _("新規")
        ON_GOING = 2, _("作業中")
        COMPLETED = 3, _("完了")

    class Progress(models.IntegerChoices):
        ZERO = 1, _("0%")
        TEN = 2, _("10%")
        TWENTY = 3, _("20%")
        THIRTY = 4, _("30%")
        FORTY = 5, _("40%")
        FIFTY = 6, _("50%")
        SIXTY = 7, _("60%")
        SEVENTY = 8, _("70%")
        EIGHTY = 9, _("80%")
        NINETY = 10, _("90%")
        HUNDRED = 11, _("100%")

    id = models.UUIDField("ID", default=uuid4, primary_key=True, editable=False)
    title = models.CharField("タイトル", max_length=100)
    description = models.CharField("説明", max_length=300)
    status = models.IntegerField(
        "ステータス", choices=Status.choices, default=Status.NOT_STARTED
    )
    progress = models.IntegerField(
        "進捗", choices=Progress.choices, default=Progress.ZERO
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="カテゴリー"
    )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="task_owner", verbose_name="タスク作成者"
    )
    started_at = models.DateTimeField("タスク開始時間", null=True, blank=True)
    total_time = models.IntegerField("合計作業時間", default=0, null=True, blank=True)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)

    def __str__(self):
        return self.title
