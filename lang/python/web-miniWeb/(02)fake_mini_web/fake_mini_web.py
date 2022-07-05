"""框架(处理动态请求)"""
import time

#假WSGI框架
def login():
    return "<h2>登录界面</h2>"

def center():
    return "<h1>主页面</h1>"

def application(filename):
    if filename == "login":
        return login()
    elif filename == "center":
        return center()
    else:
        return "<h1>NOT FOUND!!! %s </h1>" % time.ctime()