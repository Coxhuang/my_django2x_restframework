from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework import serializers
from faker import Faker
from wordcloud import WordCloud
import numpy as np
from django.conf import settings
import base64

fake_obj = Faker(locale='zh_CN') # 生成一个Faker对象(中文),默认不传参数时为英文


# *******************************************************************************
# *                                                                             *
# * @标题  : 我的序列化-应用层
# * @功能  : 序列化方法
# * @备注  : None
# *                                                                             *
# *******************************************************************************
class MySerializerApp(DynamicFieldsMixin,serializers.ModelSerializer):

    def create_cloudword_base64(self, circle, width, tag, color, full):
        """
        生成云词图
        :param circle: 是否是圆形
        :param width: 大小
        :param tag: 关键字
        :param color: 背景颜色
        :param full: 是否填充
        :return: 云词图base64
        """

        tag_str = "" # 空格隔开
        tag = eval(tag)
        if isinstance(tag, list):
            for foo in tag:
                tag_str = " ".join((tag_str,foo))

        if circle: # 圆形

            x, y = np.ogrid[:width, :width]
            mask = (x - int(width/2)) ** 2 + (y - int(width/2)) ** 2 > int(width/2) ** 2
            mask = 255 * mask.astype(int)
        else:
            mask = None  # 设置默认

        wordshow = WordCloud(
            background_color=color,
            width=width,
            height=width,
            repeat= full,
            mask=mask,
            font_path=settings.FONTPATH,
        ).generate(tag_str)

        path = "".join((settings.MEDIA_ROOT,"/images/cloudword/temp.png"))
        wordshow.to_file(path)
        with open(path,"rb") as f:
            base64_data = base64.b64encode(f.read()).decode()

        return base64_data

    def get_fake_obj(self):
        """
        获取fake对象
        :return: fake_obj
        """
        return fake_obj

