# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/21 17:46
@Auth ： Minhang
@File ：config.py
@IDE  ：PyCharm
"""

from django.conf import settings

class RedisConfig(object):
    """
    Redis配置
    """

    def __init__(self, **kwargs):

        if settings.DEV_EVN: # 本地开发环境
            self.HOST = "127.0.0.1"
            self.PORT = "6379"
            self.DB = 0
        else:
            self.HOST = "127.0.0.1"
            self.PORT = "6379"
            self.DB = 1

config_redis = RedisConfig()