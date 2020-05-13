from django.utils.deprecation import MiddlewareMixin
from utils.common.exceptions import exception
from utils.common.logs.log import LogsBase

# *******************************************************************************
# *                                                                             *
# * @标题  : 系统中间件
# * @功能  : 系统中间件
# * @备注  : None
# *                                                                             *
# *******************************************************************************
class MySystemMiddleware(MiddlewareMixin):  # 继承Middlewaremixin
    pass
    # def process_exception(self, request, exceptions):
    #     print("request:",request)
    #     print(exceptions,type(exceptions))


    # def process_response(self, request, response):
    #     print(response)
    #
    #     return response

    # def process_request(self, request):
    #     print("This is process_request : ", request.user)
    #
    #     return None

    # def process_view(self, request, callback, callback_args, callback_kwargs):
    #     print("This is process_view : ", request.user)


class ApiLoggingMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)
        LogsBase.output_logger(request,response) # 记录日志

        return response
