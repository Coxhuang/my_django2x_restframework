import base64

# *******************************************************************************
# *                                                                             *
# * @标题  : 文件类
# * @功能  : 关于文件操作 封装的方法
# * @备注  : None
# *                                                                             *
# *******************************************************************************
class FileBase(object):

    @classmethod
    def image_to_base64(cls,file_handle):
        """
        将图片转成base64
        :param file_handle: 文件句柄
        :return: base64
        """
        if file_handle:
            base64_data = base64.b64encode(file_handle.read()).decode()
        else:
            base64_data = None

        return base64_data # 'data:image/jpeg;base64,%s' % base64_data

