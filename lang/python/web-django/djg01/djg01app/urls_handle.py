from django.conf.urls import url
from .views import *
#   匹配服务器传来的url
urlpatterns = [
    url(r'.*index.*',index),            # 只要有index就使用views.py中的index函数
    url(r'.*center.*',center),
    url(r".*",index)
]