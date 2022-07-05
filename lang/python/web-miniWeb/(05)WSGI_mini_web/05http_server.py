"""
http服务器:
    1.创建tcp服务器套接字
    2.修改服务器套接字(端口绑定、被动监听状态)
    3.接收客户端的请求
    4.为客户端服务(请求分析、数据回复)
"""
#读取配置文件来指明使用的http服务器的ip、port、框架位置、临时文件的文件夹、js/css/html文件的文件夹
import socket
import re
import multiprocessing
import sys

class WSGIServer(object):
    def __init__(self,ip="127.0.0.1",port=8080,frame_app_name=None):
        #创建服务器tcp套接字
        self.server_tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #修改为重复使用
        self.server_tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #修改为非堵塞
        #self.server_tcp_socket.setblocking(False)
        #本地端口绑定
        local_addr = (ip,port)
        self.server_tcp_socket.bind(local_addr)
        #修改为监听状态
        self.server_tcp_socket.listen()
        #用户套接字表
        self.client_socket_list = list()
        self.app_frame = frame_app_name

    def set_head(self,status,head):
        status = "HTTP/1.1 %s \r\n" % status
        head = head
        #添加浏览器版本信息
        head += [("server:","laowang_web")]
        #创建http头部
        tempsave = str()
        self.back_data_head = str()
        for back_head in head:
            tempsave += back_head[0]+back_head[1]+"\r\n"
        self.back_data_head = status + tempsave
        return self.back_data_head


    def server2client(self,client_socket):
        while True:
            #接受客户端发来的请求
            request = client_socket.recv(1024).decode("utf-8")
            #如果有请求且请求不为空
            if request:
                #http数据切割
                request_data = request.splitlines()
                #re分析
                request_filename = re.match(r"^([^/]*)/(.*)( HTTP/1.1)$",request_data[0])
                request_filename = request_filename.group(2)
                print(request_filename)
                if request_filename.isspace() or request_filename==str():                    #如果全为空格或为空字符串
                   request_filename = "index.html"
                print("（服务器打印）请求文件:--------------->{0}<-------------------".format(request_filename))
                #本地数据查找(调用框架实现)
                dic = dict()
                dic["PATH_INFO"] = request_filename
                back_data_body = self.app_frame(dic,self.set_head)
                back_data = self.back_data_head+"\r\n"+back_data_body
                #数据回传
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
                proc= multiprocessing.Process(target=self.server2client,args=(client_socket,))
                proc.start()
            if client_socket in self.client_socket_list:
                while client_socket in self.client_socket_list:
                    self.client_socket_list.remove(client_socket)


# 用于整个程序的控制
def main():
    #配置说明的字典
    config_dict = dict()
    # 配置文件的读取与解析
    try:
        with open("./conf.ini") as config:
            configs = config.read().splitlines()
            for config in configs:
                if re.match("^(ip)=(.*)$",config):
                    ip = re.match("^(ip)=(.*)$",config).group(2)
                elif re.match("^(port)=(.*)$",config):
                    port = int(re.match("^(port)=(.*)$",config).group(2))
                elif re.match("^(dynamic)=(.*)$", config):
                    dynamic = re.match("^(dynamic)=(.*)$", config).group(2)
                elif re.match("^(static)=(.*)$", config):
                    static = re.match("^(static)=(.*)$", config).group(2)
                elif re.match("^(tempsave)=(.*)$", config):
                    tempsave = re.match("^(tempsave)=(.*)$", config).group(2)
                elif re.match("^(FrameName)=(.*)$", config):
                    FrameName = str(re.match("^(FrameName)=(.*)$", config).group(2))
        config_dict["ip"] = ip
        config_dict["port"] = port
        config_dict["dynamic"] = dynamic
        config_dict["static"] = static
        config_dict["tempsave"] = tempsave
        config_dict["FrameName"] = FrameName
    #配置文件有误时
    except:
        print("ERROR!!!")
        print("配置文件有误!!!")
        print("请按照以下格式写cong.ini配置文件(不可颠倒顺序):")
        error_text = str('''
                        ip="127.0.0.1"
                        port=8080
                        dynamic=dynamic
                        static=static
                        tempsave=tempsave
                        FrameName=mini_web_4
                    ''')
        print(error_text)
    """
        经过尝试有时提前导入模块(无论时在外部main函数中导入，还是在class类中设置属性)，解决方法:什么时候使用什么时候导入
        eg:
            #需要在run函数中使用module_A中的set函数
            def run():
                ret = __import__(module_A)      #返回module_A的引用
                func = ret.set()                #返回module_A中set函数的引用
    """
    # 导入框架
    sys.path.append(dynamic)       #系统中添加框架所在的环境变量
    ret_module = __import__(FrameName)     #__import__()导入模块，返回导入的模块对象
    application = getattr(ret_module,"application")   #getattr(模块引用，模块中的函数名)，返回指定模块中函数的引用

    #创建WSGI对象
    wsgi = WSGIServer(ip=ip,port=port,frame_app_name=application)
    #调用run_forever方法
    wsgi.run_forever()


if __name__ == "__main__":
    main()