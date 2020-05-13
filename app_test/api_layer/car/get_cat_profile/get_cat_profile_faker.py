# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/9 11:33
@Auth ： Minhang
@File ：get_cat_profile_faker.py
@IDE  ：PyCharm
"""

from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from app_user.api_layer.user.create_user.create_user_serializer import CreateUserSerializer
from app_test.app_layer.view import AppTestCreateModeMixin
from app_user.sql_layer.sql_business import AppUserSqlBusiness
from rest_framework.response import Response
from rest_framework import status
from app_car import models
import random

class FakerCarProfileApi(AppTestCreateModeMixin):
    authentication_classes = ()  # 验证 authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = ()  # 权限 permission_classes = (permissions.IsAuthenticated,)
    queryset = AppUserSqlBusiness.get_all_userprofile() # 所有用户信息
    # serializer_class = CreateUserSerializer
    msg_create = "批量生成车辆假数据-成功"  # 提示信息
    results_display = False

    def create(self, request, *args, **kwargs):

        for foo in range(100):

            obj_car = models.CarProfile.objects.create(
                job_status = random.randint(0,6),
                mileage = random.randint(0,10000),
                soc = random.randint(0,100),
                veh_id = "P0"+str(random.randint(10,99)),
                veh_status = random.randint(0,1),
                vehicle_frame_num = "ad do amet laboris tempor",
                vehicle_number = "津A 123456",
                vehicle_type = "in cillum dolore",
            )
            range_count = random.randint(1, 4)
            for fo in range(range_count):
                models.CarSensor.objects.create(
                    car_id=obj_car,
                    sensor_type="camera",
                    sensor_detail="xxx",
                    sn="SN0001" + str(random.randint(10000, 99999))
                )

        return Response({
            "success": True,
            "msg": self.msg_create,
            "results": []
        }, status=status.HTTP_201_CREATED)


