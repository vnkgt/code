"""
http服务器:
    1.创建tcp服务器套接字
    2.修改服务器套接字(端口绑定、被动监听状态)
    3.接收客户端的请求
    4.为客户端服务(请求分析、数据回复)
"""

import socket
import re
import threading
import fake_mini_web


class WSGIServer(object):
    def __init__(self,ip="127.0.0.1",port=8080):
        #创建服务器tcp套接字
        self.server_tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #修改为重复使用
        self.server_tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #修改为非堵塞
        #self.server_tcp_socket.setblocking(False)
        #本地端口绑定
        self.ip = ip
        self.port = port
        local_addr = (self.ip,self.port)
        self.server_tcp_socket.bind(local_addr)
        #修改为监听状态
        self.server_tcp_socket.listen()
        #用户套接字表
        self.client_socket_list = list()

    def server2client(self,client_socket):
        while True:
            #接受客户端发来的请求
            request = client_socket.recv(1024).decode("utf-8")
            #如果有请求且请求不为空
            if request:
                #http数据切割
                request_data = request.splitlines()
                #re分析
                request_filename = re.match(r"^([^/]*)/(.*)(HTTP/1.1)$",request_data[0])
                request_filename = str(request_filename.group(2))
                #本地数据查找
                if request_filename.isspace() or request_filename==str():                    #如果全为空格或为空字符串
                   request_filename = "center"
                print("本地文件:", request_filename)
                back_file = fake_mini_web.application(filename=request_filename)
                back_data_head = "HTTP/1.1 200 OK\r\n"
                back_data = back_data_head + "\r\n" +back_file
                print(back_data)
                client_socket.send(back_data.encode("utf-8"))

            #请求为空
            else:
                print("已经断开!!!")
                #关闭用户套接字
                client_socket.close()
                while client_socket in self.client_socket_list:
                    # 用户表移除套接字
                    self.client_socket_list.remove(client_socket)
                #停止接受信息
                break

    def run_forever(self):
        print("Main process is running!!!")
        while True:
            #接收客户端的请求并创建客户端套接字
            client_socket,client_addr = self.server_tcp_socket.accept()            #client_socket.setblocking(False)
            if not client_socket in self.client_socket_list:
                #添加到用户套接字表
                self.client_socket_list.append(client_socket)
                #调用函数为客户端服务(多线程)
                thread = threading.Thread(target=self.server2client,args=(client_socket,))
                thread.start()
            if client_socket in self.client_socket_list:
                while client_socket in self.client_socket_list:
                    self.client_socket_list.remove(client_socket)


# 用于整个程序的控制
def main():
    #创建WSGI对象
    wsgi = WSGIServer(ip="192.168.0.102")
    #调用run_forever方法
    wsgi.run_forever()


if __name__ == "__main__":
    main()