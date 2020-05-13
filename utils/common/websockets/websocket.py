# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/11 11:43
@Auth ： Minhang
@File ：websocket.py
@IDE  ：PyCharm
"""
from utils.common.logs.log import LogsBase
from rest_framework.response import Response
from rest_framework import status
import json
import timeout_decorator
from data.global_enums import GetGlobalEnum


websocket_ret_data = {
    "success":True,
    "msg":"pong",
    "results":{},
}

class MyDwebSocket(LogsBase):
    """封装webSocket(基于dwebsocket)"""

    def __init__(self):
        pass

    @classmethod
    def accept_dwebsocket(cls, request=None):

        def wrapper(func):

            def inner_wrapper(*args, **kwargs):

                if request.is_websocket():
                    cls.logging(data="websocket请求")

                    @timeout_decorator.timeout(GetGlobalEnum.WEBSOCKET_TIME_OUT.value,use_signals=False)
                    def ws_func():
                        for message in request.websocket:  # 客户端刷新/关闭时, message 为 None
                            if message:
                                serializer = func(*args, **kwargs)
                                serializer.data["success"] = True
                                serializer.data["msg"] = "pong"
                                request.websocket.send(json.dumps(serializer.data))
                            else:
                                cls.logging(data="退出websocket")
                                break
                    try:
                        ws_func()
                    except:
                        websocket_ret_data["success"] = False
                        websocket_ret_data["msg"] = "未检测到客户端心跳, 服务端主动关闭websocket连接"
                        request.websocket.send(json.dumps(websocket_ret_data))
                        cls.logging(data="未检测到客户端心跳, 服务端主动关闭websocket连接")

                else: # http 请求
                    serializer = func(*args, **kwargs)

                    return Response(serializer.data, status=status.HTTP_200_OK)

            return inner_wrapper

        return wrapper


@MyDwebSocket.accept_dwebsocket()
def a():
    print("haha")

if __name__ == "__main__":
    a()





