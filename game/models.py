from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    score = models.IntegerField(default=0, verbose_name="Очки")
    level = models.IntegerField(default=1, verbose_name="Уровень")

    class Meta:
        verbose_name = "Игрок"
        verbose_name_plural = "Игроки"




