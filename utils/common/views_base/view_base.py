from django.shortcuts import get_object_or_404
from utils.common.exceptions import exception
from utils.common.logs.log import LogsBase

class MyViewBase(LogsBase):

    throttle_scope = 'throttle_base_30_Min'  # 节流每分钟30次

    def __init__(self):
        pass

    def validation_error(self, serializer):
        """
        自定义序列化捕获异常函数
        :param serializer: 序列化后的对象
        :return: None
        """
        try:
            ret = serializer.is_valid(raise_exception=True)  # 捕获异常
        except Exception as e:
            print("序列化异常处理函数,e:{}".format(e))
            dict_exception = e.__dict__.get("detail", "")
            if "success" in dict_exception:
                self.msg_error = dict_exception["msg"]
            else:
                for i, v in dict_exception.items():
                    self.msg_detail = i
                    self.msg_error = v[0]
                    break  # 只获取第一个异常结果
            raise exception.myException400({
                # "success": False,
                "msg": "{}".format(self.msg_error),  # 异常消息
                "results": {
                    "field": self.msg_detail,  # 具体异常的字段
                    "detail": self.msg_error,  # 异常消息
                }
            })
        return None

    def get_object_base(self, model, field):
        """
        获取对象
        :param field: 字段
        :param model: 模型
        :return: instance
        """

        try:
            instance = get_object_or_404(model, username=field)

        except:
            raise exception.myException400({
                # "success": False,
                "msg": "获取instance异常",
                "results": ""
            })

        return instance


