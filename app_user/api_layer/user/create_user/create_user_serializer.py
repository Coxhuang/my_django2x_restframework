# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/8 18:00
@Auth ： Minhang
@File ：create_user_serializer.py
@IDE  ：PyCharm
"""
from rest_framework import serializers
from app_user import models
from app_user.app_layer.serializer import AppUserSerializer

class CreateUserSerializer(AppUserSerializer):

    username = serializers.CharField(
        label="用户名",
        help_text="用户名",
        required=True,
        allow_null=False,
        allow_blank=False,
        error_messages=AppUserSerializer.field_error_msg(field="用户名")
    )
    password = serializers.CharField(
        label="密码",
        help_text="密码",
        required=True,
        allow_null=False,
        allow_blank=False,
        error_messages=AppUserSerializer.field_error_msg(field="密码")
    )
    role = serializers.IntegerField(
        label="角色",
        help_text="角色",
        required=False,
        error_messages=AppUserSerializer.field_error_msg(field="角色")
    )

    class Meta:
        model = models.UserProfile
        fields = ["username", "password", "role", ]

    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(
            **validated_data
        )
        return user







