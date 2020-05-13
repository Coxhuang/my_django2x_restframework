# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/8 19:23
@Auth ： Minhang
@File ：login_user_serializer.py
@IDE  ：PyCharm
"""
from rest_framework import serializers

from utils.common.serializers_base.serializer_base import MySerializerBase
from app_user import models

class LoginUserSerializer(MySerializerBase):

    username = serializers.CharField(
        label="用户名",
        help_text="用户名",
        required=True,
        allow_null=False,
        allow_blank=False,
        error_messages=MySerializerBase.field_error_msg(field="用户名")
    )
    password = serializers.CharField(
        label="密码",
        help_text="密码",
        required=True,
        allow_null=False,
        allow_blank=False,
        error_messages=MySerializerBase.field_error_msg(field="密码")
    )

    class Meta:
        model = models.UserProfile
        fields = ["username","password",]