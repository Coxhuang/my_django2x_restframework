from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.db.backends.signals import connection_created
from django.db.models.signals import pre_migrate, post_migrate
from django.core.signals import request_finished
from django.core.signals import request_started
from django.core.signals import got_request_exception
from django.db.models.signals import class_prepared
from django.db.models.signals import pre_init, post_init
from django.db.models.signals import pre_save, post_save
from django.db.models.signals import pre_delete, post_delete
from django.db.models.signals import m2m_changed
from django.db.models.signals import pre_migrate, post_migrate
from django.test.signals import setting_changed
from django.test.signals import template_rendered
from django.db.backends.signals import connection_created
from app_user.models import UserProfile
from data.global_enums import GetUserConfig
from utils.common.logs.log import LogsBase



class SignalsBusinessFunc(object):
    """信号量业务函数"""

    @classmethod
    def create_superadmin(cls):
        superadmin_username = GetUserConfig.SUPERADMIN_USERNAME.value
        superadmin_password = GetUserConfig.SUPERADMIN_PASSWORD.value
        superadmin_email = GetUserConfig.SUPERADMIN_EMAIL.value
        superadmin_obj = UserProfile.objects.filter(
            username=superadmin_username
        )
        if not superadmin_obj.exists():
            UserProfile.objects.create_superuser(
                username=superadmin_username,
                password=superadmin_password,
                email=superadmin_email,
                role=0,
            )
            LogsBase.logging("新增超级管理员:{}".format(superadmin_username), level="collect")

        return None

    @classmethod
    def create_admin(cls):
        admin_username = GetUserConfig.ADMIN_USERNAME.value
        admin_password = GetUserConfig.ADMIN_PASSWORD.value
        admin_email = GetUserConfig.ADMIN_EMAIL.value
        admin_obj = UserProfile.objects.filter(
            username=admin_username
        )
        if not admin_obj.exists():
            UserProfile.objects.create_superuser(
                username=admin_username,
                password=admin_password,
                email=admin_email,
                role=1,
            )
            LogsBase.logging("新增管理员:{}".format(admin_username), level="collect")

        return None

    @classmethod
    def create_user(cls):
        username = GetUserConfig.USERNAME.value
        password = GetUserConfig.PASSWORD.value
        email = GetUserConfig.EMAIL.value
        user_obj = UserProfile.objects.filter(
            username=username
        )
        if not user_obj.exists():
            UserProfile.objects.create_superuser(
                username=username,
                password=password,
                email=email,
                role=2,
            )
            LogsBase.logging("新增用户:{}".format(username), level="collect")

        return None



# *******************************************************************************
# *                                                                             *
# * @标题  : 信号量
# * @功能  : 信号量
# * @备注  : None
# *                                                                             *
# *******************************************************************************
@receiver(post_migrate)
def callback_post_migrate(sender, **kwargs):
    """
    数据库迁移命令执行之后
    :param sender:
    :param kwargs:
    :return:
    """

    if sender.name == "app_user": # 当用户表发生数据库迁移时, 检测数据库中是否已经存在超级管理员, 不存在就新增
        SignalsBusinessFunc.create_superadmin() # 新增超级管理员
        SignalsBusinessFunc.create_admin() # 新增管理员
        SignalsBusinessFunc.create_user() # 新增普通用户

    return None

