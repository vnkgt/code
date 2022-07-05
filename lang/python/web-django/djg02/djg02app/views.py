from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader,RequestContext  # 用来处理模板文件(处理html文件)
from .models import BookInfo,HeroInfo

def re_render(request,templ_name,temp_dict):
    # 1.获取模板
    load_get = loader.get_template(templ_name)
    # 2.渲染获取html文件
    re_result = load_get.render(temp_dict)
    # 3.html返回
    return HttpResponse(re_result)

# Create your views here.
def index(request):
    return re_render(request,"index.html",{})

def show_books(request):
    books_name = BookInfo.objects.all()
    return re_render(request,"books.html",{"books":books_name})

def show_hero_in_books(request,book_id):
    #1.获取对应book_id的book
    hero_book = BookInfo.objects.get(id=book_id)
    #2.获取和hero_book相关联的英雄
    hero_name = HeroInfo.objects.filter(hbook=hero_book)
    return re_render(request,"hero_in_books.html",{"heros":hero_name,"hbook":hero_book})