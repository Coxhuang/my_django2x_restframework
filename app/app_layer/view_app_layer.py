from app.utils.common.mixins.view_minxin import MyCreateModeMixin
from app.utils.common.mixins.view_minxin import MyDeleteModelMixin
from app.utils.common.mixins.view_minxin import MyUpdateModelMixin
from app.utils.common.mixins.view_minxin import MyListModelMixin
from app.utils.common.mixins.view_minxin import MyRetrieveModelMixin


class AppCreateModeMixin(MyCreateModeMixin):
    pass

class AppDeleteModelMixin(MyDeleteModelMixin):
    pass

class AppUpdateModelMixin(MyUpdateModelMixin):
    pass

class AppListModelMixin(MyListModelMixin):
    pass

class AppRetrieveModelMixin(MyRetrieveModelMixin):
    pass