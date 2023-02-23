from uuid import uuid4

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Meta:
        verbose_name = "ユーザー"
        verbose_name_plural = "ユーザー"

    id = models.UUIDField("ID", default=uuid4, primary_key=True, editable=False)


def upload_avatar_path(instance, filename):
    extension = filename.split(".")[-1]
    return "/".join(
        ["avatars", str(instance.user_profile.id) + str(".") + str(extension)]
    )


class Profile(models.Model):
    class Meta:
        verbose_name = "プロフィール"
        verbose_name_plural = "プロフィール"

    id = models.UUIDField("ID", default=uuid4, primary_key=True, editable=False)

    user_profile = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name="user_profile",
        on_delete=models.CASCADE,
        verbose_name="プロフィールユーザー",
    )
    avatar = models.ImageField(
        "アバター", blank=True, null=True, upload_to=upload_avatar_path
    )

    def __str__(self):
        return self.user_profile.username
