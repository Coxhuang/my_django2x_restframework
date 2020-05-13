from rest_framework.pagination  import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict
import math
from data.global_enums import GetPaginationConfig



# *******************************************************************************
# *                                                                             *
# * @标题  : 自定义分页
# * @功能  : DRF提供的自定义分页
# * @备注  : None
# *                                                                             *
# *******************************************************************************
class MyPagination(PageNumberPagination):

    msg_list = "ok"
    page_size = GetPaginationConfig.PAGE_SIZE.value    # 每页最多显示数量
    page_size_query_param = GetPaginationConfig.PAGE_SIZE_QUERY_PARAM.value # 可以通过传入 /api/xxx/?page=2,改变默认每页显示的个数
    max_page_size = GetPaginationConfig.MAX_PAGE_SIZE.value # 最大页数不超过500
    page_query_param = GetPaginationConfig.PAGE_QUERY_PARAM.value # 可以通过传入 /api/xxx/?page=2, 获取指定页数据

    def get_total_pages(self):
        """总页数"""
        return math.ceil(self.page.paginator.count / self.page_size)  # 向上取整

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            # ('success', True),  # 成功标志
            ('msg', self.msg_list),  # 消息
            ('count', self.page.paginator.count), # 数量
            ('size', self.page_size), # 每页大小
            ('totalpages', self.get_total_pages()), # 总页数
            # ('next', self.get_next_link()), # 下一页地址
            # ('previous', self.get_previous_link()), # 上一页地址
            ('results', data) # 返回数据
         ]))

