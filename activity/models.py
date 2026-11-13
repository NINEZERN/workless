from typing import ClassVar

from django.conf import settings
from django.db import models
from django.db.models import Q, UniqueConstraint
from django.utils import timezone


# Create your models here.
class PlaySession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    started_at = models.DateTimeField(default=timezone.now)
    finished_at = models.DateTimeField(null=True, blank=True)
    objects = models.Manager()

    class Meta:
        constraints: ClassVar = [
            UniqueConstraint(
                fields=["user"],
                condition=Q(finished_at__isnull=True),
                name="unique_user_session"
                )

        ]
