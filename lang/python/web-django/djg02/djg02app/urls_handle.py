from django.conf.urls import url
from .views import *

urlpatterns = [
    url(".*index.*",index),
    url("^books$",show_books),
    url("^books/(\d+)$",show_hero_in_books),
    url(".*",index),
]