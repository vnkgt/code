from django.shortcuts import render
from django.http.request import QueryDict

# Create your views here.
def login(request):
    #   template_name:html模板的名字     context:传给html模板的参数字典
    return render(request,template_name="login.html",context={"log":"hahaha"})

def login_check(request):
    """登录检查"""
    #   request是QueryDict对象
    #   QueryDict属性与字典相似
    #   在python manage.py shell中运行以下代码
    # q = QueryDict("a=1&b=2&c=3")
    # q.get('a')
    # q.get('b')
    #
    # q1 = QueryDict("a=1&a=2&a=3")
    # q1.getlist('a')

    #   1.获取用户名和密码
    username = request.POST.get("username")
    password = request.POST.get("password")

    result = str()
    #   2.登录校验
    if username=="vmkjack" and password=="123":
        result = "True"
    else:
        result = "False"

    #   3.结果返回
    return render(request,template_name="login_check.html",context={"result":result})
