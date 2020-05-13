# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/8 19:17
@Auth ： Minhang
@File ：login_user_view.py
@IDE  ：PyCharm
"""
# -*- coding: utf-8 -*-

from rest_framework.response import Response
from rest_framework import status
from app_user.api_layer.login.login_user_serializer import LoginUserSerializer
from app_user.app_layer.view import AppUserCreateModeMixin
from app_user.sql_layer.sql_business import AppUserSqlBusiness


class LoginUserApi(AppUserCreateModeMixin):
    authentication_classes = ()  # 验证 authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = ()  # 权限 permission_classes = (permissions.IsAuthenticated,)
    queryset = AppUserSqlBusiness.get_all_userprofile() # 所有用户信息
    serializer_class = LoginUserSerializer
    msg_create = "登录-成功"  # 提示信息

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        self.validation_error(serializer=serializer)  # 自定义Serializer异常处理

        username = request.data.get("username", "")
        password = request.data.get("password", "")

        self.check_auth_base( # 校验用户名和密码
            username=username,
            password=password,
        )

        instance = self.get_object_base( # 获取用户对象
            model=AppUserSqlBusiness.get_all_userprofile(),
            field=username,
        )

        token = self.create_token_base(user=instance) # 生成 TOKEN

        return Response({
            # "success": True,
            "msg": self.msg_create,
            "results": {
                "username": username,
                "TOKEN":token,
            }
        }, status=status.HTTP_200_OK)


