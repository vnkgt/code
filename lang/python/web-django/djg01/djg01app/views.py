from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext  # 用来处理模板文件(处理html文件)

#   用来处理html模板文件
#   fun_request:视图函数获取的request参数    template_name:模板文件名(路径已经配置好)    template_args_dict:要传递给模板文件的参数字典
def re_render(fun_request_arg , template_name , template_args_dict):
    # 1.加载模板文件，模板对象
    loder_get = loader.get_template(template_name=template_name)
    # # 2.定义模板上下问(经过测试此步貌似多余)
    # context = RequestContext(fun_request_arg,template_args_dict)
    # 3.渲染html文件,参数替换
    # res_html = loder_get.render(context)
    res_html = loder_get.render(template_args_dict)
    # 4.返回html对象给浏览器
    return HttpResponse(res_html)


# Create your views here.
def index(request):
    """请求index时返回"""
    # return HttpResponse("This is index in djg01app.views")

    # # 1.加载模板文件，模板对象
    # loder_get = loader.get_template(template_name="index.html")
    # # # 2.定义模板上下问
    # # context = RequestContext(request,{"arg_html1":"参数"})
    # # 3.渲染html文件,参数替换
    # res_html = loder_get.render({"arg_html1":"参数1,由views.py中的index函数传递"})
    # # 4.返回html对象给浏览器
    return re_render(request,"index.html",{"arg_html1":"参数1,由views.py中的index函数传递","html_list":list(range(0,18))})


def center(request):
    return HttpResponse("This is center in djg01app.views")
