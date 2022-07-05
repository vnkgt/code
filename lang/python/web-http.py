"""
    服务器的效率:
        epoll(单任务实现多任务的效果，底层在操作系统)> 协程(单任务实现多任务的效果，底层在程序内部)> 多线程> 多进程

    操作系统中一切皆文件:
        1)键盘、鼠标、显示器、打印机都为文件
        2)操作系统通过读写文件实现复杂的功能
        3)文件在操作系统中都有一个文件描述符fd(File Descriptor)本质是一个数字，可通过fd找到相应的文件




    HTTP协议(基于TCP协议)(http一种传输信息的规定格式):
        客户端(浏览器)发送请求(GET /addr HTTP/http_version)----->服务器回应请求，将数据发送到客户端(HTTP/http_version 200(or 404) OK(or eeror))


        客户端请求的数据格式:
        Request:
            GET /addr HTTP/1.1             (HTTP版本1.1   addr:请求的数据的在服务器当中的地址(可有可无))   必须有改行
            Host: www.baidu.com             服务器地址
            Connection: keep-alive          连接方式
            Cache-Control: max-age=0
            Upgrade-Insecure-Requests: 1
            User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36         客户端(浏览器)的信息
            Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9     可接收的文件
            Sec-Fetch-Site: none
            Sec-Fetch-Mode: navigate
            Sec-Fetch-User: ?1
            Sec-Fetch-Dest: document
            Accept-Encoding: gzip, deflate, br                           接收的解码格式
            Accept-Language: zh-CN,zh;q=0.9                               可接收的语言种类(eg:中文、英文等)
            Cookie: BIDUPSID=D9EB0CF3650D2EAE771A38F1D27D1A0A; PSTM=1587998203; BAIDUID=D9EB0CF3650D2EAEACCAA1D1EB2553E5:FG=1; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; yjs_js_security_passport=f11c7ebf914a3119dc99ef31b7ac9a82423a547a_1588395871_js; BD_HOME=1; H_PS_PSSID=1449_31169_21097_31427_31341_31464_31228_30824_26350_31163
            (Cookie代表用户浏览的信息)

        服务器回传数据的格式
        Response:（header和body中间空一行来区分，"header"和"body"两个说明并不会在传输回来的数据中显示）
    header: HTTP/1.1 200 OK                  (HTTP版本1.1   200 OK代表有请求的页面(404代表请求失败))     必须要有该行
            Bdpagetype: 1
            Bdqid: 0x811f3f4f003c9387
            Cache-Control: private
            Connection: keep-alive
            Content-Encoding: gzip
            Content-Type: text/html;charset=utf-8
            Date: Sun, 03 May 2020 02:12:16 GMT
            Expires: Sun, 03 May 2020 02:11:33 GMT
            Server: BWS/1.1
            Set-Cookie: BDSVRTM=0; path=/
            Set-Cookie: BD_HOME=1; path=/
            Set-Cookie: H_PS_PSSID=1449_31169_21097_31427_31341_31464_31228_30824_26350_31163; path=/; domain=.baidu.com
            Strict-Transport-Security: max-age=172800
            Traceid: 158847193628491701869304224963709670279
            X-Ua-Compatible: IE=Edge,chrome=1
            Transfer-Encoding: chunked

        body:xxxxxxxxxxxxxxxxxxxxx(内容数据，body与header之间空一行代表为body数据区,从该行开始)
            xxxxxxxxxxxxxxxxxxxxxxx
            xxxxxxxxxxxxxxxxxxxx



    eg：
        客户端:
            GET / HTTP/1.1

        服务器:(在实际编程当中换行使用\r\n否者会出现不兼容的问题)
            HTTP/1.1 200 OK

            <h1>hahaha</h1>      发回数据hahaha




        短链接与长链接:
            短链接:    客户端请求多次数据，每请求一次，创建一个tcp链接
            长链接:    客户端请求多次数据，只创建一次tcp链接
                长连接需要在数据头部添加:
                    Collection:keep-alive         确保是长连接
                    Content-Length:数据长度         说明数据长度




        epoll:单线程，效率比协程高（在python中epoll可使用select模块实现）
            实现的方法:  创建一个特殊的内存空间，该空间可以被程序和操作系统访问(一般情况下程序空间和操作系统的空间是分开的)，
                        通过消息通知(监测是否有消息，以及消息的fd)的方法取代轮询(轮流询问有无消息)
                        消息通知:   有需要则显示
                        轮询:        挨个询问是否有需要




"""


import gevent
import socket            #网络
import threading         #多线程
import multiprocessing
import re
import os
import select




"""1)固定网页回复的http服务器"""


# def client_server(client_socket):
#     #打印用户(浏览器)请求
#     client_request = client_socket.recv(1024)
#     print(client_request)
#
#     #给用户发送数据
#     back_data_header = "HTTP/1.1 200 OK\r\n"
#     back_data_header += "\r\n"
#     back_data_body = "<h1>FUCK YOU!!!</h1>"
#     back_data = back_data_header+back_data_body
#     client_socket.send(back_data.encode("utf-8"))
#
#     #关闭用户套接字
#     client_socket.close()
#
#
# def  main():
#     """实现http协议的简易服务器"""
#     #创建tcp套接字
#     http_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
#     #绑定本地端口(本地计算机当服务器)
#     local_addr =  ("",6789)
#     http_server_socket.bind(local_addr)
#
#     #修改为监听状态
#     http_server_socket.listen()
#     while True:
#         #接收用户的请求，创建用户套接字
#         client_sockt, client_addr = http_server_socket.accept()
#
#         #为用户服务
#         client_server(client_sockt)
#
#
# if __name__ == "__main__":
#     main()



"""2)可以显示页面的服务器"""
# def client_serv_fun(client_sockt):
#     # 接收用户的数据请求并分析
#     client_request = client_sockt.recv(1024)
#     client_request = client_request.decode("GBK")
#     client_request_list = client_request.splitlines()   # 将请求数据分割
#
#     # 本地文件查找
#     back_data_list = []
#     try:
#         # 匹配请求的文件
#         request_local_file = client_request_list[0]
#         request_local_file = re.match(r"^([^/]*)/([^ ]*)( HTTP/1.1)", request_local_file)
#         request_local_file = request_local_file.group(2)
#         #本地查找请求的文件
#         if request_local_file == None:
#             request_local_file = "1.txt"
#         back_local_file = open("htmls/"+request_local_file,"r")
#         #本地存在请求的文件
#         back_data_head = "HTTP/1.1 200 OK\r\n"
#         back_data_body = back_local_file.read()
#         back_data_list.append(back_data_head)
#         back_data_list.append(back_data_body)
#     except:
#         # 本地不存在请求的文件
#         back_data_head = "HTTP/1.1 200 OK\r\n"
#         back_data_body = "未在服务器找到该文件!!!"
#         back_data_list.append(back_data_head)
#         back_data_list.append(back_data_body)
#     back_data = back_data_list[0] + "\r\n" + back_data_list[1]
#
#     # 数据回传
#     back_data = back_data.encode("GBK")
#     client_sockt.send(back_data)
#
#
#
# def main():
#     """创建一个可以接受用户请求并显示页面的服务器"""
#     # 创建tcp套接字
#     http_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     http_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
#     # 绑定端口
#     local_addr = ("",6789)
#     http_server_socket.bind(local_addr)
#
#     # 修改为监听模式
#     http_server_socket.listen()
#
#     # 接收用户请求并创建用户套接字
#     client_socket, client_addr = http_server_socket.accept()
#
#     # 为用户服务
#     client_serv_fun(client_socket)
#
#
# if __name__ == "__main__":
#     main()


"""3)mutiprocessing多进程服务器"""
# def client_serv_fun(client_sockt):
#     # 接收用户的数据请求并分析
#     client_request = client_sockt.recv(1024)
#     client_request = client_request.decode("GBK")
#     client_request_list = client_request.splitlines()   # 将请求数据分割
#
#     # 本地文件查找
#     back_data_list = []
#     try:
#         # 匹配请求的文件
#         request_local_file = client_request_list[0]
#         request_local_file = re.match(r"^([^/]*)/([^ ]*)( HTTP/1.1)", request_local_file)
#         request_local_file = request_local_file.group(2)
#         #本地查找请求的文件
#         if request_local_file == None:
#             request_local_file = "1.txt"
#         back_local_file = open("htmls/"+request_local_file,"r")
#         #本地存在请求的文件
#         back_data_head = "HTTP/1.1 200 OK\r\n"
#         back_data_body = back_local_file.read()
#         back_data_list.append(back_data_head)
#         back_data_list.append(back_data_body)
#     except:
#         # 本地不存在请求的文件
#         back_data_head = "HTTP/1.1 200 OK\r\n"
#         back_data_body = "未在服务器找到该文件!!!"
#         back_data_list.append(back_data_head)
#         back_data_list.append(back_data_body)
#     back_data = back_data_list[0] + "\r\n" + back_data_list[1]
#
#     # 数据回传
#     back_data = back_data.encode("GBK")
#     client_sockt.send(back_data)
#
#     client_sockt.close()
#
#
#
# def main():
#     """创建一个可以接受用户请求并显示页面的服务器"""
#     # 创建tcp套接字
#     http_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     http_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
#     # 绑定端口
#     local_addr = ("",6789)
#     http_server_socket.bind(local_addr)
#
#     # 修改为监听模式
#     http_server_socket.listen()
#
#     # 为用户服务
#     while True:
#         # 接收用户请求并创建用户套接字
#         client_socket, client_addr = http_server_socket.accept()
#
#         p =  multiprocessing.Process(target=client_serv_fun,args=(client_socket,))
#         p.start()
#         client_socket.close()
#
#
# if __name__ == "__main__":
#     main()



"""4)threading多线程实现服务器"""
# def client_serv_fun(client_sockt):
#     # 接收用户的数据请求并分析
#     client_request = client_sockt.recv(1024)
#     client_request = client_request.decode("GBK")
#     client_request_list = client_request.splitlines()   # 将请求数据分割
#
#     # 本地文件查找
#     back_data_list = []
#     try:
#         # 匹配请求的文件
#         request_local_file = client_request_list[0]
#         request_local_file = re.match(r"^([^/]*)/([^ ]*)( HTTP/1.1)", request_local_file)
#         request_local_file = request_local_file.group(2)
#         #本地查找请求的文件
#         if request_local_file == None:
#             request_local_file = "1.txt"
#         back_local_file = open("htmls/"+request_local_file,"r")
#         #本地存在请求的文件
#         back_data_head = "HTTP/1.1 200 OK\r\n"
#         back_data_body = back_local_file.read()
#         back_data_list.append(back_data_head)
#         back_data_list.append(back_data_body)
#     except:
#         # 本地不存在请求的文件
#         back_data_head = "HTTP/1.1 200 OK\r\n"
#         back_data_body = "未在服务器找到该文件!!!"
#         back_data_list.append(back_data_head)
#         back_data_list.append(back_data_body)
#     back_data = back_data_list[0] + "\r\n" + back_data_list[1]
#
#     # 数据回传
#     back_data = back_data.encode("GBK")
#     client_sockt.send(back_data)
#
#     client_sockt.close()
#
#
#
# def main():
#     """创建一个可以接受用户请求并显示页面的服务器"""
#     # 创建tcp套接字
#     http_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     http_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
#     # 绑定端口
#     local_addr = ("",6789)
#     http_server_socket.bind(local_addr)
#
#     # 修改为监听模式
#     http_server_socket.listen()
#
#     # 为用户服务
#     while True:
#         # 接收用户请求并创建用户套接字
#         client_socket, client_addr = http_server_socket.accept()
#
#         t =  threading.Thread(target=client_serv_fun,args=(client_socket,))
#         t.start()
#
# if __name__ == "__main__":
#     main()




"""5)gevent协程实现服务器"""
# def client_serv_fun(client_sockt):
#     # 接收用户的数据请求并分析
#     client_request = client_sockt.recv(1024)
#     client_request = client_request.decode("GBK")
#     client_request_list = client_request.splitlines()   # 将请求数据分割
#
#     # 本地文件查找
#     back_data_list = []
#     try:
#         # 匹配请求的文件
#         request_local_file = client_request_list[0]
#         request_local_file = re.match(r"^([^/]*)/([^ ]*)( HTTP/1.1)", request_local_file)
#         request_local_file = request_local_file.group(2)
#         #本地查找请求的文件
#         if request_local_file == None:
#             request_local_file = "1.txt"
#         back_local_file = open("htmls/"+request_local_file,"r")
#         #本地存在请求的文件
#         back_data_head = "HTTP/1.1 200 OK\r\n"
#         back_data_body = back_local_file.read()
#         back_data_list.append(back_data_head)
#         back_data_list.append(back_data_body)
#     except:
#         # 本地不存在请求的文件
#         back_data_head = "HTTP/1.1 200 OK\r\n"
#         back_data_body = "未在服务器找到该文件!!!"
#         back_data_list.append(back_data_head)
#         back_data_list.append(back_data_body)
#     back_data = back_data_list[0] + "\r\n" + back_data_list[1]
#
#     # 数据回传
#     back_data = back_data.encode("GBK")
#     client_sockt.send(back_data)
#
#     client_sockt.close()
#
#
# def main():
#     """创建一个可以接受用户请求并显示页面的服务器"""
#     # 创建tcp套接字
#     http_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     http_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
#     # 绑定端口
#     local_addr = ("",6789)
#     http_server_socket.bind(local_addr)
#
#     # 修改为监听模式
#     http_server_socket.listen()
#
#     # 为用户服务
#
#     while True:
#         # 接收用户请求并创建用户套接字
#         client_socket, client_addr = http_server_socket.accept()
#         g = gevent.spawn(client_serv_fun,client_socket)
#         g.join()
#
# if __name__ == "__main__":
#     main()




"""6)协程、非堵塞"""


# def server_client(client_socket):
#     back_file_list = []
#     try:
#         # 获取用户消息
#         request = client_socket.recv(1024)
#
#         # 用户请求信息提取
#         request = request.splitlines()
#         request = request[0].decode("utf-8")
#         # re匹配所需文件
#         request_file = re.match(r"^([^/]*)/([^ ]*) (HTTP/1.1)$",request)
#         request_file = request_file.group(2)
#         with open("htmls/"+request_file) as back_file:
#             back_body = back_file.read()
#             back_head = "HTTP/1.1 200 OK\r\n"
#             back_file_list.append(back_head)
#             back_file_list.append(back_body)
#     except:
#         back_head = "HTTP/1.1 404 NOT FOUND\r\n"
#         back_body = "<h1>未在服务器找到所需内容!!!</h1>"
#         back_file_list.append(back_head)
#         back_file_list.append(back_body)
#
#     back_data = back_file_list[0]+"\r\n"+back_file_list[1]
#     back_data = back_data.encode("GBK")
#
#     client_socket.send(back_data)
#
#     # 关闭用户套接字
#     client_socket.close()
#
#
# def main():
#     """协程服务器"""
#     # 创建套接字
#     http_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
#     # 设置服务器套接字为非堵塞状态，一旦堵塞则报错
#     http_server_socket.setblocking(False)
#
#     # 端口绑定
#     local_add = ("",6789)
#     http_server_socket.bind(local_add)
#
#     # 设置端口可以重复使用
#     http_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
#     # 设置监听状态
#     http_server_socket.listen()
#
#     while True:
#         try:
#             # 获取并生成用户套接字
#             client_socket, client_addr = http_server_socket.accept()
#
#             # 设置用户套接字为非堵塞状态，一旦堵塞则报错
#             client_socket.setblocking(False)
#
#             # 协程为用户服务
#             g = gevent.spawn(server_client,client_socket)
#             g.join()
#
#         except:
#             pass
#
#
#
# if __name__ == "__main__":
#     main()




"""7)单任务、非堵塞、长链接实现http"""

# def server_client(client_socket, client_req):
#     # client_request数据分割获取请求数据列表
#     request = client_req.splitlines()
#
#     # re提取用户所需的文件名
#     request_file = re.match(r"^([^/]*)/([^ ]*) (HTTP/1.1)$",request[0])
#     request_file = request_file.group(2)
#
#     try:
#         # 本地文件查找
#         with open("htmls/"+request_file,"br") as back_file:
#             # 本地文件读取
#             back_data_body = back_file.read().decode("GBK")
#             back_data_head = "HTTP/1.1 200 OK\r\n"
#             back_data_head += "Collection:keep-alive\r\n"
#             back_data_head += "Content-Length:%d\r\n" % len(back_data_body)
#             back_data = back_data_head + "\r\n" + back_data_body
#             # 数据(编码并)回传
#             client_socket.send(back_data.encode("GBK"))
#     except:
#         back_data_body = "<h1>未找到指定文件!!!</h1>"
#         back_data_head = "HTTP/1.1 404 NOT FOUND\r\n"
#         back_data_head += "Collection:keep-alive\r\n"
#         back_data_head += "Content-Length:%d\r\n" % len(back_data_body)
#         back_data = back_data_head + "\r\n" + back_data_body
#         # 数据(编码并)回传
#         client_socket.send(back_data.encode("GBK"))
#
#
#
#
# def main():
#     # 1.创建服务器套接字
#     http_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     # 1.1端口绑定
#     local_addr = ("",6789)
#     http_server_socket.bind(local_addr)
#     # 1.2设置非堵塞模式
#     http_server_socket.setblocking(False)
#     # 1.3改为监听模式
#     http_server_socket.listen()
#     # 1.3(01)设置端口可以重复使用
#     http_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
#     client_socket_list = list()
#     while True:
#         try:
#             # 1.4获取用户请求并创建用户套接字
#             client_socket, client_addr = http_server_socket.accept()
#             # 1.5修改用户套接字为非堵塞状态
#             client_socket.setblocking(False)
#
#             # 2向用户套接字列表中添加获取的新用户套接字
#             client_socket_list.append(client_socket)
#
#         except:
#             pass
#
#         for num in range(len(client_socket_list)):
#             try:
#                 # 2.1获取用户的请求的数据(并解码)
#                 client_request = client_socket_list[num].recv(1024).decode("GBK")
#             except:
#                 pass
#             else:
#                 if client_request:      # 空数据传回也是有数据
#                     # 2.2分析用户请求并回传数据
#                     server_client(client_socket_list[num], client_request)
#
#                 else:  # 无数据传回,判断客户端是否已断开链接
#                     # 关闭客户端套接
#                     client_socket_list[num].close()
#                     # 列表中移除关闭的套接字
#                     client_socket_list.remove(client_socket_list[num])
#                     print(client_socket_list[num],"已断开链接!!!")
#
# if __name__ == "__main__":
#     main()




"""8)epoll单任务http(Linux系统中运行)"""
# import select
# import socket
# import re
#
# def server_client(socket, request_data):
#     request = request_data.splitlines() # 数据切割
#     request_file = re.match("^([^/]*)/([^ ]*) HTTP/1.1$",request[0]).group(2)  # re匹配
#     # 本地查找文件
#     try:
#         back_file = open("htmls/"+request_file)
#         back_data_body = back_file.read()+"\r\n"
#         back_data_body = back_data_body*30
#         back_data_head = "HTTP/1.1 200 OK\r\n"
#         back_data_head += "Content-Length:%d\r\n" % len(back_data_body)
#         back_data_head += "Content-Length:%d\r\n" % len(back_data_body)
#         back_data = back_data_head + "\r\n" + back_data_body
#         socket.send(back_data.encode("utf-8"))
#     except:
#         back_data_head = "HTTP/1.1 404 NOT FOUND\r\n"
#         back_data_body = "为找到相关文件!!!"
#         back_data_head += "Content-Length:%d\r\n" % len(back_data_body)
#         back_data = back_data_head + "\r\n" + back_data_body
#         socket.send(back_data.encode("GBK"))
#
# def main():
#     # 创建套接字,端口绑定,监听状态,套接字重复使用
#     http_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     local_addr = ("",6789)
#     http_server_socket.bind(local_addr)
#     http_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     http_server_socket.listen()
#
#
#     # 获取用户套接字，创建epoll，用户套接字注册，套接字对应相应的fd
#     epl = select.epoll()
#     fd_socket_dict = dict()
#
#     epl.register(http_server_socket.fileno(),select.EPOLLIN)
#     fd_socket_dict[http_server_socket.fileno()] = http_server_socket
#
#     while True:
#         event_pol = epl.poll()
#         for fd, event in event_pol:
#             # 字典中的监听套接字
#             if fd == http_server_socket.fileno():
#                 client_socket, client_addr = http_server_socket.accept()
#                 epl.register(client_socket.fileno(),select.EPOLLIN)
#                 fd_socket_dict[client_socket.fileno()] = client_socket
#             # 用户套接字
#             elif event == select.EPOLLIN:
#                 client_socket = fd_socket_dict[fd]
#                 client_request = client_socket.recv(1024).decode("utf-8")
#                 if client_request:  # 有请求信息
#                     server_client(client_socket, client_request)
#                 else:   # 连接断开
#                     print("CLOSED:",fd_socket_dict[fd])
#                     client_socket.close()
#                     epl.unregister(fd)
#                     del fd_socket_dict[fd]
#
#     # 监听套接字关闭
#     http_server_socket.close()
#
# if __name__ == "__main__":
#     print("START!!!")
#     main()
#     print("END!!!")
