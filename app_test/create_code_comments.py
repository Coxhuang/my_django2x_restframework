# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/29 07:41
@Auth ： Minhang
@File ：create_code_comments.py
@IDE  ：PyCharm
"""


class CodeComments(object):
    """
    创建代码注释规范
    """

    def __init__(self):
        self.title = "# * @标题  : "
        self.function = "# * @功能  : "
        self.remark = "# * @备注  : "
        self.margin = "# *******************************************************************************"
        self.padding = "# *                                                                             *"
        self.content_list = []

    def create_tools_comments(self):
        """
        创建工具注释
        :return: string
        """
        self.title += input("请输入 标题 : ")
        self.function += input("请输入 功能 : ")
        self.remark += input("请输入 备注 : ")
        count = 1
        while True:
            content = input("请输入 说明(输入0退出) : ")
            if content == "0" :
                break
            print_str = "# * #说明{} : {}".format(count + 1, content)
            self.content_list.append(print_str)



        print(self.margin)
        print(self.padding)
        print(self.title)
        print(self.function)
        print(self.remark)

        for foo in self.content_list:
            print(foo)


        print(self.padding)
        print(self.margin)

        return None
"""
# *********************************************************************
# *                                                                   *
# * @标题  : 跨域配置
# * @功能  : 解决前后端分离跨域问题
# * @备注  : 看一下说明,有几个需要注意的地方
# * #说明1 : 在settings.py文件中添加中间件 corsheaders.middleware.CorsMiddleware
# * #说明2 : 中间件corsheaders.middleware.CorsMiddleware必须放在第三的位置,不能任意放
# *                                                                   *
# *********************************************************************
"""

    # def create_code_comments(self):
    #     """
    #     创建code注释
    #     :return: string
    #     """


if __name__ == "__main__":
    obj = CodeComments()
    obj.create_tools_comments()