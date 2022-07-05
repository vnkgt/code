"""djg01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

#   匹配客户端传来的url(浏览器传来的url的参数(参数:除去IP地址和port端口号的部分))
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^',include('djg01app.urls_handle')),    # 除请求"admin/"外全部转向djg01app.urls_handle中判断
]
