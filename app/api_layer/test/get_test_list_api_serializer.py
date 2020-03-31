from app.app_layer.serializer_app_layer import AppSerializerApp
from rest_framework import serializers
from app import models

class GetTestListSerializer(AppSerializerApp):

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






