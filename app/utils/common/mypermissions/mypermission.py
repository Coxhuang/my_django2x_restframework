from rest_framework.permissions import BasePermission

# *******************************************************************************
# *                                                                             *
# * @标题  : 自定义权限
# * @功能  : 自定义权限
# * @备注  : 使用请看说明
# * @说明1  : permission_classes = (permissions.IsMyAdminUser,)
# * @说明2  : has_permission(self, request, view)方法返回True时, 认为有权限
# *                                                                             *
# *******************************************************************************
class IsMyAdminUser(BasePermission):

    def has_permission(self, request, view):
        """
        只允许自定义的管理员通过
        :param request:
        :param view:
        :return: bool
        """

        return True if request.user.role == 0 else False

