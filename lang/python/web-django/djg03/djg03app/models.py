from django.db import models
from django.db.models import Sum,Count,Avg,Max,Min
# Create your models here.
class BookInfo(models.Model):
    #书名
    bookname = models.CharField(max_length=20)
    #发行日期
    bookdate = models.DateField()
    #阅读量
    book_com = models.IntegerField(default=0)
    #点赞量
    book_sup = models.IntegerField(default=0)

