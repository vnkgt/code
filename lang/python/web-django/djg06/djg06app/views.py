from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.http import request

# Create your views here.
#   index页面
#   /index
def index(request):
    return HttpResponse("This is index!!!")

#   ajax + login
#   /login_ajax
def login_ajax(request):
    """返回login_ajax页面(login局部刷新页面)"""
    return render(request,"login_ajax.html")

#   /login_ajax_check
def login_ajax_check(request):
    """login_ajax登录校验页面"""
    #   1.获取用户名和密码
    username = request.POST.get("username")
    password = request.POST.get("password")
    print(username,password)
    #   2.进行校验，判断用户名以及密码是否正确(在数据表中)，返回json数据
    if username=="vmkjack" and password=="123":
        #用户名及密码正确
        return JsonResponse({"res":1})
    else:
        return JsonResponse({"res":0})

#   cookie
#   /set_cookie
def set_cookie(request):
    """设置浏览器的cookie"""
    #设置一个cookie信息
    response = HttpResponse("set_cookie:--->num:{0}".format(str(1)))
    response.set_cookie("num",1,max_age=7*24*3600)
    #返回response
    return response

#   /get_cookie
def get_cookie(request):
    """读取浏览器的cookie"""
    #读取出cookie中num的值
    num = request.COOKIES["num"]
    return HttpResponse("get_cookie:--->num:{0}".format(str(int(num)+1)))

#   cookie + login
#   /login_cookie
def login_cookie(request):
    username = str()
    """返回login_ajax页面(login局部刷新页面)"""
    if "username" in request.COOKIES:    # 保存了cookie
        username = request.COOKIES["username"]
    #数据返回
    return render(request,"login_cookie.html",{"UserName":username})

#   /login_cookie_check
def login_cookie_check(request):
    """login_ajax登录校验页面"""
    #   1.获取用户名和密码
    username = request.POST.get("username")
    password = request.POST.get("password")
    remember = request.POST.get("remember")     #   获取，用户是否选择记住用户名，的信息
    #   2.进行校验，判断用户名以及密码是否正确(在数据表中)
    if username=="vmkjack" and password=="123":
        response = HttpResponse("登录成功")
        if remember=="on":              #   用户选择记住用户名
            response.set_cookie("username",username)
        return response
    else:
        return HttpResponse("登录失败")

#   session
#   /set_session
def set_session(request):
    """设置session"""
    request.session["username"] = "ABCXVX"
    request.session["age"] = 18
    return HttpResponse("设置session")

#   /get_session
def get_session(request):
    """获取session"""
    username = request.session["username"]
    age = request.session["age"]+1
    return HttpResponse("{0}:{1}".format(username,str(age)))

#   session + login
#   /login_session
def login_session(request):
    #1.获取session
    if "username" in request.session and "password" in request.session:
        username = request.session["username"]
        password = request.session["password"]
        return render(request,"login_session.html",{"username":username,"password":password})
    #2.无session记录
    else:
        return render(request,"login_session.html",{})

#   /login_session_check
def login_session_check(request):
    #1.获取用户名密码，及是否保存session
    username = request.POST.get("username")
    password = request.POST.get("password")
    remember = request.POST.get("remember")
    print("----------------------------->",username,password,remember)
    #2.判断用户名及密码是否正确
    if username=="vmk" and password== "123":
        response = HttpResponse("登录成功")
        if remember=="on":          #判断是否保存session
            request.session["username"] = username
            request.session["password"] = password
        return response
    else:
        return HttpResponse("用户名或密码错误")

#   /session_clear
def session_clear(request):
    #   清除某个
    del request.session["username"]
    #   只清除记录
    request.session.clear()
    #  完全清除
    request.session.flush()
    return HttpResponse("清除完毕!!!")
