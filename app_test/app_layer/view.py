from utils.common.drf_mixins.view_minxin import MyCreateModeMixin
from utils.common.drf_mixins.view_minxin import MyDeleteModelMixin
from utils.common.drf_mixins.view_minxin import MyUpdateModelMixin
from utils.common.drf_mixins.view_minxin import MyListModelMixin
from utils.common.drf_mixins.view_minxin import MyRetrieveModelMixin
from faker import Faker
fake_obj = Faker(locale='zh_CN') # 生成一个Faker对象(中文),默认不传参数时为英文


class AppTestCreateModeMixin(MyCreateModeMixin):

    def get_fake_obj(self):
        """
        获取fake对象
        :return: fake_obj
        """
        return fake_obj

class AppTestDeleteModelMixin(MyDeleteModelMixin):
    pass

class AppTestUpdateModelMixin(MyUpdateModelMixin):
    pass

class AppTestListModelMixin(MyListModelMixin):
    pass

class AppTestRetrieveModelMixin(MyRetrieveModelMixin):
    pass