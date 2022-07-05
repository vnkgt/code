from django.conf.urls import url,include
from .views import *
urlpatterns = [
    url("^login&",login),
    url("^login_check$",login_check),
]