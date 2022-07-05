from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import *
# Create your views here.
#   /.*
def index(request):
    return HttpResponse("This is index!!!")

#返会上传图片的html页面
#   /client_upload_html
def client_upload_html(request):
    return render(request,"client_upload_html.html")

#保存用户图片的函数
#   /client_upload_save
def client_upload_save(request):
    #1.获取上传文件的处理对象
    img = request.FILES["client_img"]
    #2.创建一个空文件用来保存浏览传来的数据
    save_path = "{0}/{1}".format(settings.MEDIA_ROOT,"Img_Client/"+img.name)            #img.name:浏览器上传图片的名字
    #3.获取浏览器上传文件内容并写入文件
    with open(save_path,"wb") as f:
        for content in img.chunks():                                                    #img.chunks():浏览器上传图片文件数据包
            f.write(content)
    #4.在数据库中保存上传记录
    Img_Admin.objects.create(img="Img_Client/"+img.name)
    #5.返回
    return HttpResponse("上传成功!!!")
