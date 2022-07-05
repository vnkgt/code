from django.shortcuts import render,redirect
from .models import *
from datetime import date
from django.http import HttpResponseRedirect,HttpResponse
from django.template import loader

# Create your views here.
def re_render(request,template_name,template_arg_dict):
    #1.读取html文件
    loder_get = loader.get_template(template_name)
    #2.渲染
    re_result = loder_get.render(template_arg_dict)
    #3.返回
    return HttpResponse(re_result)

def BookInfo_show(request):
    """显示数的目录"""
    books = BookInfo.objects.all()
    return re_render(request,"BookInfo.html",{"books":books})

def bookinfo_add(request):
    b = BookInfo()
    b.bookname = '火影忍者'
    b.bookdate = date(1999,7,8)
    b.save()
    return HttpResponseRedirect("/books")

def bookinfo_del(request,book_id):
    #获取对象
    book = BookInfo.objects.get(id = book_id)
    #删除
    book.delete()
    return HttpResponseRedirect("/books")



def index(request):
    return HttpResponse("ok")