from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework import serializers
from app.utils.common.serializers.serializer import MySerializerApp


# *******************************************************************************
# *                                                                             *
# * @标题  : 序列化-插件
# * @功能  : 序列化方法
# * @备注  : None
# *                                                                             *
# *******************************************************************************
class MySerializerMixin(MySerializerApp):
    pass