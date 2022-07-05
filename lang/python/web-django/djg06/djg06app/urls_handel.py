from django.conf.urls import url
from .views import *

urlpatterns = [
    #   ajax + login测试
    url("^login_ajax$",login_ajax),         #   匹配登录页面
    url("^login_ajax_check$",login_ajax_check),      #   匹配login_ajax_check局部请求
    #   cookie测试
    url("^set_cookie$",set_cookie),                  #  设置cookie
    url("^get_cookie$",get_cookie),                  #  读取cookie
    #   cookie + login测试
    url("^login_cookie$",login_cookie),
    url("^login_cookie_check$",login_cookie_check),
    #   session测试
    url("^set_session$",set_session),
    url("^get_session$",get_session),
    #   session + login
    url("^login_session$",login_session),
    url("^login_session_check$",login_session_check),
    url("^session_clear$",session_clear),
    #   其他index页面
    url(".*",index),
]