#极简版mini_web框架


#env：为环境，包括http_server接收客户端请求的文件名  set_response_head：http_server服务器中一个处理http头的函数
def application(env,set_response_head):
    set_response_head("200 OK",[("Content-Type:","text/html;charset=utf-8")])
    print( "--------->%s<----------"% env["PATH_INFO"])
    if env["PATH_INFO"]=="center.html":
        return "<h1>fjasldkfjalsdjflakjsdlf</h1>"
    elif env["PATH_INFO"]=="index.html":
        return "<h1>This is index.html</h1>"
    else:
        return "<h1>NONE!!!</h1>"


