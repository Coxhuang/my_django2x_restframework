# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/9 19:21
@Auth ： Minhang
@File ：log.py
@IDE  ：PyCharm
"""

import logging as _logging
import json

logger_obj = _logging.getLogger(__name__) # 生成一个以当前文件名为名字的logger实例
collect_logger_obj = _logging.getLogger("collect") # 生成一个名为collect的logger实例

# *******************************************************************************
# *                                                                             *
# * @标题  : 日志类
# * @功能  : 关于日志操作
# * @备注  : None
# *                                                                             *
# *******************************************************************************
class LogsBase(object):

    @classmethod
    def logging(cls,  data="", level="info"):

        if level.lower() == "info":
            logger_obj.info(data)

        elif level.lower() == "debug":
            logger_obj.debug(data)

        elif level.lower() == "warning":
            logger_obj.warning(data)

        elif level.lower() == "error":
            logger_obj.error(data)

        elif level.lower() == "collect":
            collect_logger_obj.info(data)

        else:
            logger_obj.info("不在统计外围内的日志, 请及时处理后端代码 --- : ",data)

    @classmethod
    def output_logger(cls, request, response, level="info", msg=""):

        try:
            body = json.loads(request.body)
        except Exception:
            body = dict()

        if level.lower() == "info":
            output_logger = "[用户: {}][{} {} {} {}][{}][{}]".format(
                request.user, request.method, request.path, response.status_code,
                response.reason_phrase, body, msg
            )

        elif level.lower() == "error":
            output_logger = "[用户: {}][{} {} {} {}][{}][{}]".format(
                request.user, request.method, request.path, response.status_code,
                response.reason_phrase, body, msg
            )

        else:
            output_logger = "[用户: {}][{} {} {} {}][{}][{}]".format(
                request.user, request.method, request.path, response.status_code,
                response.reason_phrase, body, msg
            )

        LogsBase.logging(output_logger,level)

        return None