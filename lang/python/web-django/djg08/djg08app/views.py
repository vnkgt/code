from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
#   /index3
def index(request):
    """主页"""
    return render(request,"index.html")

#   /url_reverse
def url_reverse(request):
    """url逆向解析访问主页"""
    return render(request,"url_reverse.html")

#   /url_reverse_arg
#   先访问127.0.0.1/url_reverse点击相应链接,再手动访问127.0.0.1:8080/url_reverse_arg/77/88
def url_reverse_arg(request,place1,place2):
    """url逆向解析获取位置参数"""
    return HttpResponse("url逆向解析位置参数place1:{0}  place2:{1}".format(place1,place2))

#   /url_reverse_kwarg
#   先访问127.0.0.1/url_reverse点击相应链接,再手动访问127.0.0.1:8080/url_reverse_kwarg/34/55
def url_reverse_kwarg(request,key1,key2):
    """url逆向解析获取关键字参数"""
    return HttpResponse("url逆向解析关键字参数key1:{0}   key2:{1}".format(key1,key2))


#   静态文件
#   /static
def static(request):
    return render(request,"static.html")



