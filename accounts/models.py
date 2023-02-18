from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class Meta:
        verbose_name = "ユーザー"
        verbose_name_plural = "ユーザー"
    id = models.UUIDField("ID", default=uuid4, primary_key=True, editable=False)
