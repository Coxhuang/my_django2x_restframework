from django.urls import path
from django.urls import include
from rest_framework import routers

from app.api_layer.test.get_test_list_api_view import GetTestListApi

GetTestListApiRouter = routers.DefaultRouter()
GetTestListApiRouter.register('', GetTestListApi,base_name="")

urlpatterns = [
    path('get-test-list/', include(GetTestListApiRouter.urls)),
]
