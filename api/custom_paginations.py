from rest_framework import pagination

class MyPageNumberPagination(pagination.PageNumberPagination):
    page_size = 5
    # page_query_param = 'mypage'
    # page_size_query_param = 'size'
    # max_page_size = 10

class MyLimitOffsetPagination(pagination.LimitOffsetPagination):
    default_limit = 5
    # limit_query_param = 'mylimit'
    # offset_query_param = 'myoffset'
    # max_limit = 7 

class MyCursorPagination(pagination.CursorPagination):
    page_size = 5
    ordering = 'created_at'
    # cursor_query_param = 'mycursor'
    # page_size_query_param = 'size'
    # max_page_size = 5


class MyCustomPagination(pagination.BasePagination):
    pass

