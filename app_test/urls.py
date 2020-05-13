from django.urls import path
from django.urls import include
from rest_framework import routers

from app_test.api_layer.test.get_test_list_api_view import GetTestListApi
from app_test.api_layer.car.get_cat_profile.get_cat_profile_faker import FakerCarProfileApi

GetTestListApiRouter = routers.DefaultRouter()
GetTestListApiRouter.register('', GetTestListApi,base_name="")
FakerCarProfileApiRouter = routers.DefaultRouter()
FakerCarProfileApiRouter.register('', FakerCarProfileApi,base_name="")

urlpatterns = [
    path('get-test-list/', include(GetTestListApiRouter.urls)),
    path('create-carprofile-faker/', include(FakerCarProfileApiRouter.urls)),
]
