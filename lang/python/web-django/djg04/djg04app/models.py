from django.db import models

# Create your models here.
class ChinaManage(models.Manager):
    def all(self):
        return self.get(id=1)

class ChinaInfo(models.Model):
    #   地区名
    name = models.CharField(max_length=30)
    #   父地区
    parent_id = models.IntegerField(default=0)
    obj = ChinaManage()

    class Meta:
        db_table = 'china'  # 指定表名