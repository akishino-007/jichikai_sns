from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.json import KeyTransformTextLookupMixin


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, verbose_name="自己紹介")
    birthyear = models.IntegerField(null=True, blank=True, verbose_name="生まれ年（西暦）")
    kumi = models.IntegerField(null=True, blank=True, verbose_name="組番号（1～20）")

    def __str__(self):
        return self.username