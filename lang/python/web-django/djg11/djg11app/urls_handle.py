from django.conf.urls import url
from .views import *

urlpatterns = [
    url("^client_upload_html$",client_upload_html),     #上传文件的html
    url("^client_upload_save$",client_upload_save),     #上传文件的视图函数
    url(".*",index),
]
