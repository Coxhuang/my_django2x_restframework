from rest_framework.mixins import (
    CreateModelMixin,DestroyModelMixin,
    UpdateModelMixin,ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from app.utils.common.paginations.pagination import MyPagination
from app.utils.common.views.view import MyViewApp


# *******************************************************************************
# *                                                                             *
# * @标题  : 视图-应用层
# * @功能  : 视图应用层类
# * @备注  : None
# * @说明1  : MyCreateModeMixin --> POST -- 插入数据
# * @说明2  : MyDeleteModelMixin --> DELETE -- 删除数据
# * @说明3  : MyUpdateModelMixin --> UPDATE -- 更新数据
# * @说明4  : MyListModeMixin --> GET -- 获取数据列表
# * @说明5  : MyRetrieveModelMixin --> GET -- 获取某行数据
# * @说明6  : MyAPIView --> * -- 普通请求
# *                                                                             *
# *******************************************************************************
class MyCreateModeMixin(CreateModelMixin,GenericViewSet,MyViewApp):

    authentication_classes = (JSONWebTokenAuthentication,) # 验证
    permission_classes = (permissions.IsAuthenticated,) # 权限
    msg_create = "创建成功" # 返回时显示的消息
    results_display = True  # 是否显示序列化信息, 默认显示

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        self.validation_error(serializer=serializer)  # 自定义Serializer异常处理
        # serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)

        data = serializer.data if self.results_display else None #

        return Response({
            "success": True,
            "msg": self.msg_create,
            "results": data
        }, status=status.HTTP_201_CREATED)

    def initial(self, request, *args, **kwargs):
        super(MyCreateModeMixin, self).initial(request, *args, **kwargs)

class MyDeleteModelMixin(DestroyModelMixin,GenericViewSet,MyViewApp):

    authentication_classes = (JSONWebTokenAuthentication,)  # 验证
    permission_classes = (permissions.IsAuthenticated,)  # 权限
    msg_delete = "删除成功" # 返回时显示的消息
    lookup_field = "pk"  # 主键

    def destroy(self, request, *args, **kwargs):

        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({
            "success": True,
            "msg": self.msg_delete,
            "results": None
        }, status=status.HTTP_200_OK)

    def initial(self, request, *args, **kwargs):
        super(MyDeleteModelMixin, self).initial(request, *args, **kwargs)

class MyUpdateModelMixin(UpdateModelMixin,GenericViewSet,MyViewApp):

    authentication_classes = (JSONWebTokenAuthentication,)  # 验证
    permission_classes = (permissions.IsAuthenticated,)  # 权限
    msg_update = "修改成功"
    lookup_field = "pk"  # 主键
    results_display = True

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        self.validation_error(serializer=serializer)  # 自定义Serializer异常处理
        # serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        data = serializer.data if self.results_display else None

        return Response({
            "success": True,
            "msg": self.msg_update,
            "results": data
        }, status=status.HTTP_200_OK)

    def initial(self, request, *args, **kwargs):
        super(MyUpdateModelMixin, self).initial(request, *args, **kwargs)

class MyListModelMixin(ListModelMixin,GenericViewSet,MyViewApp):

    authentication_classes = (JSONWebTokenAuthentication,)  # 验证
    permission_classes = (permissions.IsAuthenticated,)  # 权限
    pagination_class = MyPagination  # 分页
    msg_list = "获取列表数据成功"

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response({
            "success": True,
            "msg": self.msg_list,
            "results": serializer.data
        }, status=status.HTTP_200_OK)

    def initial(self, request, *args, **kwargs):
        super(MyListModelMixin, self).initial(request, *args, **kwargs)

class MyRetrieveModelMixin(RetrieveModelMixin,GenericViewSet,MyViewApp):

    authentication_classes = (JSONWebTokenAuthentication,)  # 验证
    permission_classes = (permissions.IsAuthenticated,)  # 权限
    msg_detail = "获取详细数据成功"
    lookup_field = "pk"  # 主键

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response({
            "success": True,
            "msg": self.msg_detail,
            "results": [serializer.data] # 以列表的格式返回
        }, status=status.HTTP_200_OK)

    def initial(self, request, *args, **kwargs):
        super(MyRetrieveModelMixin, self).initial(request, *args, **kwargs)

class MyAPIView(APIView,MyViewApp):

    authentication_classes = (JSONWebTokenAuthentication,)  # 验证
    permission_classes = (permissions.IsAuthenticated,)  # 权限
    msg_api = "POST API"

    # def post(self,request):
    #     # serializer = self.get_serializer(data=request.data)
    #     # self.validation_error(serializer=serializer)  # 自定义Serializer异常处理
    #     return Response({
    #         "success": False,
    #         "msg": "基类POST,请重新封装",
    #         "results": ""
    #     }, status=status.HTTP_400_BAD_REQUEST)

    def initial(self, request, *args, **kwargs):
        super(MyAPIView, self).initial(request, *args, **kwargs)
