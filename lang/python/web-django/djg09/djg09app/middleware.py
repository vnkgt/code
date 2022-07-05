from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

class TestMiddleWare(object):
    '''中间件类'''

    def __init__(self,get_response):
        '''服务器重启后接收第一个请求调用'''
        self.get_response = get_response
        print('-----init-----')

    # 想了很久才找到原因,django 3.0版本的问题
    def __call__(self, request):
        print('111111')
        return self.get_response(request)

    def process_request(self,request):
        '''产生request对象之后,url匹配之前调用'''
        print('---process_request---')

    def process_view(self,request,view_func,view_args,view_kwargs):
        '''url匹配之后,在Django调用视图之前被调用'''
        print('----process_view---')

    # def process_template_response(self,request, response):
    def process_response(self, request, response):
        '''视图函数调用之后,内容返回浏览器之前'''
        print('---process_response---')
        return response

    def process_exception(self,request,exception):
        """出现异常时调用"""
        return HttpResponse(exception)