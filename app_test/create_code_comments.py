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
        self.title = "# * @标题 : "
        self.function = "# * @功能 : "
        self.remark = "# * @备注 : "
        self.margin = "# *********************************************************************"
        self.padding = "# *                                                                   *"
        self.content_list = []

    def create_tools_comments(self):
        """
        创建工具注释
        :return: string
        """
        self.title += input("请输入 标题 : ")
        self.function += input("请输入 功能 : ")
        self.remark += input("请输入 备注 : ")
        while True:
            content = input("请输入 说明 : ")
            if content == "0" :
                break
            self.content_list.append(content)

        print(self.margin)
        print(self.padding)
        print(self.title)
        print(self.function)
        print(self.remark)
        for index, foo in enumerate(self.content_list):
            print("# * #说明{} : {}".format(index+1, foo))

        print(self.padding)
        print(self.margin)

        return None

    def create_code_comments(self):
        """
        创建code注释
        :return: string
        """


if __name__ == "__main__":
    obj = CodeComments()
    obj.create_tools_comments()