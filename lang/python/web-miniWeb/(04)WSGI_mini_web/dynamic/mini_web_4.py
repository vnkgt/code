def index():
    return "<h1>This is Index!!!</h1>"

def center():
    return "<h1>This is Center!!!</h1>"

def login():
    return "<h1>This is Login!!!</h1>"

def application(env,set_head_func):
    set_head_func("200 OK",[("Content-Type:","text/html;charset=utf-8")])
    if env["PATH_INFO"] == "index.html":
        body = index()
    elif env["PATH_INFO"] == "center.html":
        body = center()
    elif env["PATH_INFO"] == "login.html":
        body = login()
    else:
        body = "<h1>本地文件不在！！！</h1>"
    return body

def test():
    print("Successful import mini_web__4!!!")