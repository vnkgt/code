from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *                   #   导入模型类
from django.core.paginator import Paginator     #   导入分页类

# Create your views here.
#   /.*
def index(request):
    return HttpResponse("This is index!!!")

#分页测试
#   /show_area
def show_area(request,pag_num):         #   pag_num:获取请求的页码,默认为第一页
    #1.获取地区信息
    areas = China_AreaInfo.objects.filter(parent=0)
    #2.分页，每页10个
    pag = Paginator(object_list=areas,per_page=10)
    #3.获取第一页的内容
    if pag_num=="":         #   没有传页码,默认页码为1
        p_index = 1
    else:
        p_index = int(pag_num)
    return_pag = pag.page(number=p_index)
    #4.模板返回
    return render(request,"show_area.html",{"areas":return_pag})

#ajax省市县选择
#   /area_selector
def area_selector(request):
    return render(request,"area_selector.html")

#   /province           #   返回省选择处理
def province(request):
    #1.获取省份信息
    areas = China_AreaInfo.objects.filter(parent=0)
    #2.变量areas拼接出json数据:id,name
    areas_json_list = list()
    for area in areas:
        areas_json_list.append((area.id,area.name))
    #3.数据返回
    return JsonResponse({"province_data":areas_json_list})

#   /city               #   返回市选择处理
def city(request,province_id):
    #1.获取province_id对应的市
    areas = China_AreaInfo.objects.filter(parent = province_id)
    #2.遍历输出json数据
    areas_json_list = list()
    if int(province_id)==0:
        pass
    else:
        for area in areas:
            areas_json_list.append((area.id,area.name))
    #3.数据返回
    return JsonResponse({"city_data":areas_json_list})

#   /county             #   返回县选择处理
def county(request,city_id):
    #1.获取province_id对应的市
    areas = China_AreaInfo.objects.filter(parent = city_id)
    #2.遍历输出json数据
    areas_json_list = list()
    for area in areas:
        areas_json_list.append((area.id,area.name))
    #3.数据返回
    return JsonResponse({"county_data":areas_json_list})