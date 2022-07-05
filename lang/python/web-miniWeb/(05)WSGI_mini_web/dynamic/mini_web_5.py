"""
带参数的修饰器实现路由功能:
    路由:
        每添加一个新文件读取函数时使用修饰器，向全局文件字典中自动添加相应的文件函数
    路由的主要目的:
        通过全局字典的键值对来判断是否存在本地文件，减少判断语句的书写
"""
#本地文件文件读取函数字典
GLOBAL_URL_DIC = dict()
#路由修饰器
def route(func_name):
    def dic_add_dec(func_name_pointer):
        GLOBAL_URL_DIC[func_name] = func_name_pointer()
    return dic_add_dec

@route("index.html")
def index():
    return "<h1>This is Index!!!</h1>"

@route("center.html")
def center():
    return "<h1>This is Center!!!</h1>"

@route("login.html")
def login():
    return "<h1>This is Login!!!</h1>"

def application(env,set_head_func):
    try:
        set_head_func("200 OK", [("Content-Type:", "text/html;charset=utf-8")])
        return GLOBAL_URL_DIC[env["PATH_INFO"]]
    except:
        set_head_func("404 NOT FOUND", [("Content-Type:", "text/html;charset=utf-8")])
        return "<h1>NOT EXIST IN LOCAL!!!</h1>"


#测试mini_web.py是否导入成功
def test():
    print("Successful import mini_web__4!!!")