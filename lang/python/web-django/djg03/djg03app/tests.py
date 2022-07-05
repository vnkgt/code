from django.test import TestCase

# Create your tests here.
from datetime import date
from .models import *
book1 = BookInfo()
book1.bookname = "七龙珠"
book1.bookdate = date(1997,1,1)
book1.save()

book2 = BookInfo()
book2.bookname = "海贼王"
book2.bookdate = date(2000,1,1)
book2.save()