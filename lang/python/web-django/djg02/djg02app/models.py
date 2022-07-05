from django.db import models

# Create your models here.
class BookInfo(models.Model):
    bookname = models.CharField(max_length=30)
    bookdate = models.DateField()

    def __str__(self):
        return self.bookname

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hage = models.IntegerField(null=True, blank=True, default=None)
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)

    def __str__(self):
        return self.hname
