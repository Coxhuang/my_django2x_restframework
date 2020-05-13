# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/8 11:17
@Auth ： Minhang
@File ：global_enums.py
@IDE  ：PyCharm
"""

from enum import Enum
from config.data.init_data import config_redis

class GetRedisConfig(Enum):
    """"""

    HOST = config_redis.HOST
    PORT = config_redis.PORT
    DB = config_redis.DB

class GetPaginationConfig(Enum):

    PAGE_SIZE = 20 # 每页最多显示数量
    PAGE_SIZE_QUERY_PARAM = "size" # 可以通过传入 /api/xxx/?size=10,改变默认每页显示的个数
    MAX_PAGE_SIZE = 100 # 最大页数不超过100
    PAGE_QUERY_PARAM = "page"  # 可以通过传入 /api/xxx/?page=2, 获取指定页数据

class GetUserConfig(Enum):
    """初始化数据库,自动生成用户所需要的数据"""

    SUPERADMIN_USERNAME = "superadmin" # 超级管理员
    SUPERADMIN_PASSWORD = "superadmin123456"
    SUPERADMIN_EMAIL = "superadmin@minhung.me"

    ADMIN_USERNAME = "admin" # 管理员
    ADMIN_PASSWORD = "admin123456"
    ADMIN_EMAIL = "admin@minhung.me"

    USERNAME = "user" # 普通用户
    PASSWORD = "user123456"
    EMAIL = "user@minhung.me"

class GetGlobalEnum(Enum):

    WEBSOCKET_TIME_OUT = 10 # webSocket 超时时间





# if "__main__" == __name__:
#     print(GetPaginationConfig.MY_MAX_PAGE_SIZE.value)
