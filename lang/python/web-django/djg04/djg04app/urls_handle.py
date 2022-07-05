from django.conf.urls import url
from .views import *

urlpatterns = [
    url("^area$",area),
    url("center/(\d+)",center),                 #   url捕获，位置参数，参数为\d+匹配的结果
    url("personal/(?P<number>\d+)",personal),   #   url捕获，关键字参数，关键字为number,参数为\d+匹配的结果
    url(".*",index),
]
