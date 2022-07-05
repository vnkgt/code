from django.conf.urls import url
from .views import *

app_name='djg08app'

urlpatterns = [
    #直接访问首页
    url("^index3$",index,name="index"),     #   直接访问127.0.0.1:8080/index3

    #url逆向解析访问首页
    url("^url_reverse$",url_reverse),       #   直接访问127.0.0.1:8080/url_reverse

    #url逆向解析获取位置参数
    #   先访问127.0.0.1/url_reverse点击相应链接,再手动访问127.0.0.1:8080/url_reverse_arg/77/88
    url("^url_reverse_arg/(\d+)/(\d+)$",url_reverse_arg,name="url_reverse_arg"),

    #url逆向解析获取关键字参数
    #   先访问127.0.0.1/url_reverse点击相应链接,再手动访问127.0.0.1:8080/url_reverse_kwarg/34/55
    url("^url_reverse_kwarg/(?P<key1>\d+)/(?P<key2>\d+)$",url_reverse_kwarg,name="url_reverse_kwarg"),

    #静态文件加载
    url("^static$",static),
]