from django.contrib import admin

# Register your models here.
from .models import BookInfo
from .models import HeroInfo

#   自定义模型管理类,用来管理显示哪些内容在后台页面上
class BookInfoAdim(admin.ModelAdmin):
    """图书(BookInfo表)模型管理类"""
    #list_display为固定写法
    list_display = ["bookname","bookdate"]

class HeroInfoAdim(admin.ModelAdmin):
    """英雄(HeroInfo表)模型管理类"""
    list_display = ["hname","hage","hbook"]

admin.site.register(BookInfo,BookInfoAdim)   #  在后台admin页面注册BoookInfo,用BookInfoAdim修饰显示的内容
admin.site.register(HeroInfo,HeroInfoAdim)   #  在后台admin页面注册HeroInfo,用HeroInfoAdim修饰显示的内容


