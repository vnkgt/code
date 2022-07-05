from djg02app.models import *
from datetime import date

book1 = BookInfo()
book1.bookname = "天龙八部"
book1.bookdate = date(1997,4,15)
book1.save()

book2 = BookInfo()
book2.bookname = "倚天屠龙记"
book2.bookdate = date(2001,7,22)
book2.save()

book3 = BookInfo()
book3.bookname = "神雕侠侣"
book3.bookdate = date(1998,4,11)
book3.save()

book4 = BookInfo()
book4.bookname = "七龙珠"
book4.bookdate = date(1998,5,28
                      )
book4.save()

hero1 = HeroInfo()
hero1.hname = "喜羊羊"
hero1.hage = 9
hero1.hbook = book1
hero1.save()

hero2 = HeroInfo()
hero2.hname = "派大星"
hero2.hage = 15
hero2.hbook = book2
hero2.save()

hero3 = HeroInfo()
hero3.hname = "海绵宝宝"
hero3.hage = 14
hero3.hbook = book2
hero3.save()

hero4 = HeroInfo()
hero4.hname = "懒羊羊"
hero4.hage = 8
hero4.hbook = book1
hero4.save()

hero5 = HeroInfo()
hero5.hname = "美羊羊"
hero5.hage = 9
hero5.hbook = book1
hero5.save()

hero6 = HeroInfo()
hero6.hname = "韦小宝"
hero6.hage = 22
hero6.hbook = book3
hero6.save()