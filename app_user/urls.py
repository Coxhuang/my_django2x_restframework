from django.urls import path
from django.urls import include
from rest_framework import routers

from app_user.api_layer.user.create_user.create_user_view import CreateUserApi
from app_user.api_layer.login.login_user_view import LoginUserApi


CreateUserApiRouter = routers.DefaultRouter()
CreateUserApiRouter.register('', CreateUserApi,base_name="")
LoginUserApiRouter = routers.DefaultRouter()
LoginUserApiRouter.register('', LoginUserApi,base_name="")

urlpatterns = [
    path('create-user/', include(CreateUserApiRouter.urls)),
    path('login-user/', include(LoginUserApiRouter.urls)),
]
