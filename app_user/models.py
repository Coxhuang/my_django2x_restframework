from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    role_choice = (
        (0, "超级管理员"),
        (1, "管理员"),
        (2, "普通用户"),
    )

    role = models.IntegerField(
        choices=role_choice,
        default=2,
        verbose_name="用户角色",
    )
    nickname = models.CharField(
        default="",
        max_length=64,
    )
    phone = models.CharField(
        default="",
        max_length=11,
        verbose_name="手机号码",
    )