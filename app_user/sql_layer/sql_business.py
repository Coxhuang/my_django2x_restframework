# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/8 15:00
@Auth ： Minhang
@File ：sql_business.py
@IDE  ：PyCharm
"""
from utils.common.orms.orm import QuerySetOrm
from app_user import models

class AppUserSqlBusiness(QuerySetOrm):

    @classmethod
    def get_all_userprofile(cls):
        """
        获取所有用户信息
        :return: queryset
        """

        return models.UserProfile.objects.all()

