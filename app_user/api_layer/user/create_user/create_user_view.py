# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/8 17:59
@Auth ： Minhang
@File ：create_user_view.py
@IDE  ：PyCharm
"""
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from app_user import models
from app_user.api_layer.user.create_user.create_user_serializer import CreateUserSerializer
from app_user.app_layer.view import AppUserCreateModeMixin
from app_user.sql_layer.sql_business import AppUserSqlBusiness


class CreateUserApi(AppUserCreateModeMixin):
    authentication_classes = ()  # 验证 authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = ()  # 权限 permission_classes = (permissions.IsAuthenticated,)
    queryset = AppUserSqlBusiness.get_all_userprofile() # 所有用户信息
    serializer_class = CreateUserSerializer
    msg_create = "新增用户-成功"  # 提示信息
    results_display = False
