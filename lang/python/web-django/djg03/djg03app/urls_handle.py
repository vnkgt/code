from .views import *
from django.conf.urls import include,url

urlpatterns = [
    url("^books$",BookInfo_show),
    url("^bookinfo_add$",bookinfo_add),
    url("^bookinfo_del(\d+)$",bookinfo_del),
    url('.*',index),
]
