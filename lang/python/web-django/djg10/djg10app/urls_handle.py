from django.conf.urls import url
from .views import *

urlpatterns = [
    #ajax省市县选择测试
    url("^area_selector$",area_selector),
    url("^province$",province),
    url("^city(\d+)$",city),
    url("^county(\d+)$",county),
    #分页测试
    url("^show_area(\d*)$",show_area),
    url(".*",index),
]
