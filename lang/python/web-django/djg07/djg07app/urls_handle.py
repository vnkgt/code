from django.conf.urls import url
from .views import *

urlpatterns = [
    #   模板继承测试
    url("^son$",son),
    url("^father$",father),
    #   登录校验测试，登录才能修改密码
    url("^login$",login),
    url("^login_check$",login_check),
    url("^login_change_pwd$",login_change_pwd),
    url("^login_change_pwd_middle$",login_change_pwd_middle),
    url("^login_change_pwd_check$",login_change_pwd_check),
    #   清除session
    url("^clear_session$",clear_session),
    #   验证码
    url("^get_verification_code$",get_verification_code),
    #   过滤器，模板语言测试
    url(".*",index),
]
