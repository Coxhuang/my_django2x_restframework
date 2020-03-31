from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework import serializers

# *******************************************************************************
# *                                                                             *
# * @标题  : 序列化-应用层
# * @功能  : 序列化方法
# * @备注  : None
# *                                                                             *
# *******************************************************************************
class MySerializerApp(DynamicFieldsMixin,serializers.ModelSerializer):
    pass