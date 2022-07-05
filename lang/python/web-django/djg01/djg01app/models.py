from django.db import models
"""
每添加一个模板都需要重新生成数据迁移文件，且原迁移文件不删除
"""
# Create your models here.

#一类(相当于mysql的外键表)
#创建一个模型用于生成数据表模板(相当于mysql创建表，并为表创建字段)
class BookInfo(models.Model):
    #生成表时django会自动给表添加一个主字段(ID)
    #图书的名字
    bookname = models.CharField(max_length=20)        #bookname：生成表的字段名   CharField：该字段的数据类型为字符串   max_length：字符串的最大长度
    bookdate = models.DateField()

    # def __str__(self):      #在后台显示bookname
    #     return self.bookname

#多类(相当于mysql的主要数据表)
#创建英雄模版(hname:名字  hage:年龄 hbook:出自哪本书)
#特别注意:1)此处已经通过shell在BookInfo的表中添加了书名
#          2)此模板的hbook对应BookInfo为外键
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hage = models.IntegerField()
    #关系属性字段hbook，对应的字段名hbook_id（关系属性名_id）
    hbook = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    def __str__(self):          #在后台显示hname
        return self.hname


