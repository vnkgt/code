from django.contrib import admin
from .models import *

# Register your models here.
class China_AreaInfo_StackedInline(admin.StackedInline):
    """嵌入显示的数据"""
    #   写多类的名字
    model = China_AreaInfo
    extra = 2

class China_AreaInfo_TabularInline(admin.TabularInline):
    """表格嵌入显示的表格"""
    #   写多类名字
    model = China_AreaInfo
    extra = 4

class China_AreaInfo_Admin(admin.ModelAdmin):
    """China_AreaInfo的模型管理类"""
    #每页显示的个数
    list_per_page = 10
    #显示id字段，name字段；显示模型类display方法的返回值
    list_display = ["id","name","display_name","show_parent"]
    #开启底部动作执行
    actions_on_bottom = True
    #关闭顶部动作执行
    actions_on_top = True
    #列表右侧过滤栏(name字段)
    list_filter = ["name"]
    #列表页上方搜索框(name字段)
    search_fields = ["name"]
    #排序字段
    ordering=("id",)
    #修改时显示顺序
    # fields = ["parent","name"]
    #修改时显示顺序及相应字段的其他属性
    fieldsets = (
        ("地区名称",{"fields":["name",]}),
        ("父级地区",{"fields":["parent",]}),
    )
    #数据嵌入显示(在一类中显示多类)
    inlines = [China_AreaInfo_StackedInline]
    #表格嵌入显示(在一类中显示多类)
    # inlines = [China_AreaInfo_TabularInline]
admin.site.register(China_AreaInfo,China_AreaInfo_Admin)