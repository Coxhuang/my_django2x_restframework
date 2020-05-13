from utils.common.drf_mixins.view_minxin import MyCreateModeMixin
from utils.common.drf_mixins.view_minxin import MyDeleteModelMixin
from utils.common.drf_mixins.view_minxin import MyUpdateModelMixin
from utils.common.drf_mixins.view_minxin import MyListModelMixin
from utils.common.drf_mixins.view_minxin import MyRetrieveModelMixin
from utils.common.drf_mixins.view_minxin import MyAPIView
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
from utils.common.exceptions import exception
from app_user import models

class AppUserCreateModeMixin(MyCreateModeMixin):

    def check_auth_base(self, username, password):
        """
        校验用户名和密码是否匹配
        :param username: 用户名
        :param password: 密码
        :return: bool
        """

        self.check_user_exists(username) # 校验用户是否存在
        user = authenticate(username=username, password=password)
        if not user:
            raise exception.myException400({
                "success": False,
                "msg": "账号密码不匹配",
                "results": None,
            })

        return True

    def check_user_exists(self, username):
        """
        校验用户是否存在
        :param username: 用户名
        :return:
        """
        user_list = models.UserProfile.objects.filter(username=username)
        if not user_list.exists():
            raise exception.myException400({
                "success": False,
                "msg": "用户不存在",
                "results": None,
            })

        return None

    def create_token_base(self, user):
        """
        生成token
        :param user: 用户对象
        :return: TOKEN
        """

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return token

class AppUserDeleteModelMixin(MyDeleteModelMixin):
    pass

class AppUserUpdateModelMixin(MyUpdateModelMixin):
    pass

class AppUserListModelMixin(MyListModelMixin):
    pass

class AppUserRetrieveModelMixin(MyRetrieveModelMixin):
    pass

class AppUserAPIView(MyAPIView):
    pass
