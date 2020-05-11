# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/11 11:43
@Auth ： Minhang
@File ：websocket.py
@IDE  ：PyCharm
"""
from rest_framework.response import Response
from rest_framework import status
import json


websocket_ret_data = {
    "msg":"pong",
    "results":"",
}

class MyDwebSocket(object):
    """封装webSocket(基于dwebsocket)"""

    def __init__(self):
        pass

    @classmethod
    def accept_dwebsocket(cls, request=None):

        def wrapper(func):

            def inner_wrapper(*args, **kwargs):

                if request.is_websocket():
                    for message in request.websocket:  # 客户端刷新/关闭时, message 为 None
                        if message:
                            serializer = func(*args, **kwargs)
                            websocket_ret_data["results"] = serializer.data["results"]
                            request.websocket.send(json.dumps(websocket_ret_data))
                        else:
                            break

                else: # http 请求
                    serializer = func(*args, **kwargs)
                    return Response({
                        "msg": "ok",
                        "results": serializer.data["results"]
                    }, status=status.HTTP_200_OK)

            return inner_wrapper

        return wrapper


@MyDwebSocket.accept_dwebsocket()
def a():
    print("haha")

if __name__ == "__main__":
    a()





