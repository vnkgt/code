from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader

from .models import *

def returnder(request,temp_name,temp_dict):
    #   读取模板
    loader_get = loader.get_template(temp_name)
    #   模板渲染
    re_result = loader_get.render(temp_dict)
    #   模板返回
    return HttpResponse(re_result)

# Create your views here.
def index(request):
    return HttpResponse("Index")

def area(request):
    area_son = 210000
    area_father = 1
    sons = ChinaInfo.objects.filter(parent_id = area_son)
    self = ChinaInfo.objects.get(id = area_son)
    father = ChinaInfo.objects.get(id = area_father)
    return returnder(request,"area.html",{"sons":sons,"father":father,"self":self})

def center(request,num1):
    return HttpResponse(num1)

def personal(request,number):
    return HttpResponse(number)

