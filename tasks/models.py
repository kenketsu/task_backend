from uuid import uuid4

from django.db import models


class Category(models.Model):
    id = models.UUIDField("ID", default=uuid4, primary_key=True, editable=False)
    name = models.CharField("カテゴリー名", max_length=100)

    def __str__(self):
        return self.name
