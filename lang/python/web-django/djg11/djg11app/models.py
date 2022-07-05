from django.db import models

# Create your models here.
class Img_Admin(models.Model):
    """后台页面上传图片"""
    img = models.ImageField(upload_to="Img_Admin")          #   图片上传到djg11app_img_admin数据表