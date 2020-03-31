from app.app_layer.view_app_layer import AppListModelMixin
from app.api_layer.test.get_test_list_api_serializer import GetTestListSerializer
from app.utils.common.paginations.pagination import MyPagination
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from app import models

class GetTestListApi(AppListModelMixin):
    authentication_classes = ()  # 验证 authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = ()  # 权限 permission_classes = (permissions.IsAuthenticated,)
    pagination_class = MyPagination  # 分页
    queryset = models.AppTestModels.objects.all()
    serializer_class = GetTestListSerializer
    msg_list = "查看博文列表_客户端"  # 提示信息



