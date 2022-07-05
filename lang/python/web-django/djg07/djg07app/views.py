from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from datetime import date
from PIL import Image,ImageDraw,ImageFont
import random
import io
import os
# Create your views here.
#   views.py文件所在的文件夹
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#   模拟用户名和密码
USERNAME = "vmkjack"
PWD = "123456"

#   /.*
def index(request):
    name_list = ["老王","老李",not None,"老张"]
    grade_list = [-10,20,61,70,89,101,"SB"]
    nowtime = date(1998,2,3)
    return render(request,"index.html",{"name_list":name_list,"grade_list":grade_list,"nowtime":nowtime,"mod_value":16,"add_value":1})


#   模板继承测试
#   /father
def father(request):
    return render(request,"father.html")

#   /son
def son(request):
    return render(request,"son.html")


#   登录才能修改密码
#   /login
def login(request):
    username = str()
    pwd = str()
    # 判断是否存在用户名及密码的session
    if "username" in request.session:
        username = request.session["username"]
        if "pwd" in request.session:
            pwd = request.session["pwd"]
    return render(request,template_name="login.html",context={"Username":username,"Pwd":pwd,})

#   /login_check
def login_check(request):
    #   获取用户传来的用户名及密码
    username = request.POST.get("username")
    pwd = request.POST.get("pwd")
    client_ver_code = request.POST.get("client_ver_code")   #用户验证码
    real_ver_code = request.session["real_ver_code"]        #真实验证码
    if username==USERNAME and pwd==PWD:
        if client_ver_code==real_ver_code:                  #判断验证码是否正确
            request.session["username"] = username
            request.session["pwd"] = pwd
            return redirect("/login_change_pwd_middle")
        else:
            return redirect("/login")
    else:
        return redirect("/login")

#   /login_change_pwd_middle
def login_change_pwd_middle(request):
    return render(request,"login_change_pwd_middle.html")

#   /login_change_pwd
def login_change_pwd(request):
    return render(request,"login_change_pwd.html")

#   /login_change_pwd_checks
def login_change_pwd_check(request):
    old_pwd = request.POST.get("old_pwd")
    new_pwd = request.POST.get("new_pwd")
    global PWD
    if old_pwd == PWD:
        PWD = new_pwd
        return HttpResponse("修改成功")
    else:
        return HttpResponse("老密码错误")

#   /clear_session
def clear_session(request):
    request.session.flush()
    return HttpResponse("清除session成功!!!")


#   验证码功能
#   /get_verification_code
def get_verification_code(request):
    #画布背景颜色RGB
    bgcolor = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
    #自定义画布的高和宽
    width = 100
    height = 25
    #创建画面对象
    img = Image.new(mode= "RGB",size = (width,height),color=bgcolor)
    #创建画笔对象
    draw_pen = ImageDraw.Draw(img)
    #绘制噪点
    for i in range(100):
        xy_place = (random.randrange(0,width),random.randrange(0,height))
        fill_color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        draw_pen.point(xy=xy_place,fill=fill_color)
    #验证码的备选值
    verifica_code_value = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    #随机选取四个为验证码
    result_ver_code = str()
    for i in range(0,4):
        result_ver_code += verifica_code_value[random.randint(0,len(verifica_code_value))]
    #构造字体对象
    font = ImageFont.truetype(BASE_DIR+"/font_model/font_download.ttf",23)
    font_x = [5,25,50,75]
    font_y = 2
    for i in range(0,4):
        #构造字体颜色
        fontcolor = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        #绘制四个字
        draw_pen.text(xy = (font_x[i],font_y),text=result_ver_code[i],fill = fontcolor,font =font)
    #删除画笔
    del draw_pen
    #将生成的验证码存入session,便于下一步验证码的验证
    request.session["real_ver_code"] = result_ver_code
    #将图片存入内存文件
    buf = io.BytesIO()      #开辟缓存流
    img.save(buf,"png")     #图片存入缓存流
    #将内存图片返回给客户端
    return HttpResponse(buf.getvalue(),"image/png")
