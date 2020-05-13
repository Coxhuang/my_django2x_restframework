# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/8 18:33
@Auth ： Minhang
@File ：power.py
@IDE  ：PyCharm
"""
import os
import re
import sys

class QuickOperation(object):

    def __init__(self):
        self.__set_base_abspath()

    def __output_cmd(self,  msg="", *args, **kwargs):
        """
        输出命令日志
        :param msg: 日志内容
        :return: None
        """

        print("*** 正在执行命令: {} ".format(msg).ljust(60-self.__string_chinese_count(msg),"*")) # 不够60个字符, 左边补"+"
        return None

    def __string_chinese_count(self, msg=""):
        """
        统计字符串中, 中文的个数
        :param msg: 被统计的字符串
        :return: 中文的个数
        """

        count = len(re.findall(r'[\u4E00-\u9FFF]', msg))
        if isinstance(count,int):
            return count
        elif isinstance(count,float):
            return int(count)
        else:
            return 0

    def __set_base_abspath(self):
        """
        初始化基本路径
        :return: None
        """
        self.help() # 查看使用文档
        self.project_path = os.path.abspath('.')  # server 绝对路径

        return None

    def __set(self, command):

        self.__output_cmd(command)

        return os.system(command)

    def set_command(self, command="pwd"):
        """
        设置命令 - 单条
        :param command: 命令
        :return: ret
        """

        return self.__set(command)

    def help(self):

        print("帮助文档: 删除迁移文件 -- self.del_db_migrations_files()")

        return None

    def del_db_migrations_files(self):
        """
        删除数据库迁移文件
        :return: None
        """

        for maindir, subdir, file_name_list in os.walk(self.project_path):
            if "migrations" in maindir and "__pycache__" not in maindir:
                for filename in file_name_list:
                    if "__init__.py" != filename:
                        initial_path = os.path.join(maindir, filename)  # 合并成一个完整路径
                        os.remove(initial_path) # 删除

        return None

    def set_nginx(self):
        """设置Nginx"""
        self.__output_cmd("设置Nginx")
        self.__output_cmd("启动Nginx - start")
        self.__output_cmd("停止Nginx - stop")
        self.__output_cmd("重启Nginx - reload")

        input_str = input("请输入命令: ")

        if input_str == "start":
            self.set_command("sudo nginx")
            self.__output_cmd("正在 --- 启动Nginx")
        elif input_str == "stop":
            self.set_command("sudo nginx -s stop")
            self.__output_cmd("正在 --- 停止Nginx")
        else:
            self.set_command("sudo nginx -s reload")
            self.__output_cmd("正在 --- 重启Nginx")

        return None

    def run(self, *args, **kwargs):

        if len(args) <= 1:
            return None

        arg1 = args[0][1]

        if arg1 == "deletemigrations":
            self.del_db_migrations_files() # 删除迁移文件

        return None

if __name__ == "__main__":

    QuickOperation().run(sys.argv)