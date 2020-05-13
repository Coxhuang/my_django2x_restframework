from rest_framework import serializers
from app_test import models
from app_test.app_layer.serializer import AppTestSerializer

class GetTestListSerializer(AppTestSerializer):

    # username = serializers.CharField(
    #     source="author.username",
    #     label="作者",
    # )
    # createdate = serializers.SerializerMethodField(label="创建时间")

    class Meta:
        model = models.AppTestModels
        fields = ["name",]

    # def get_createdate(self,obj):
    #
    #     return self.date_to_str(obj.createdate)






