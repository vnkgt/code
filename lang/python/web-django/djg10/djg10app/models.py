from django.db import models

# Create your models here.
class China_AreaInfo(models.Model):
    """中国地区模型类"""
    name = models.CharField(max_length=20,verbose_name="name字段地区名称")
    # parent = models.ForeignKey(to="self",on_delete = models.CASCADE)
    parent = models.ForeignKey(to="self",on_delete = models.CASCADE,default=0)

    #   表名"china_areainfo"
    class Meta:
        db_table = "china_areainfo"

    def __str__(self):      #   自动调用显示,显示名字
        return self.name

    def display_name(self):     #   list_display添加显示名字
        return self.name
    # display_name.admin_order_field = "id"       #   按id排序
    display_name.short_description = "display_name地区名称"     #   指定display_name显示的字段名称

    def show_parent(self):
        return self.parent.name
    show_parent.short_description = "父级地区"

