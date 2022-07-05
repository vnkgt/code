#   Tcp下载服务器
import socket


def server_to_client(client_socket):
    """分析用户请求并发送信息"""
    #   5.分析客户请求
    client_request_fliename = client_socket.recv(1024).decode("GBK")
    print(client_request_fliename)
    try:
        # 本地数据库寻找本地文件信息
        backfile = open("temp\\"+client_request_fliename, "br")
        backfile_data = backfile.read()

        #   6.信息回传
        if backfile_data!=None:
            client_socket.send(backfile_data)
    except:
        print("未找到该文件!!!")

    #   7.客户端口关闭
    print("用户服务器关闭!!!")
    client_socket.close()

def main():
    #   1.创建服务器套接字
    tcp_download_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #   2.绑定端口
    local_addr=("192.168.0.104",1551)
    tcp_download_server.bind(local_addr)
    #   3.修改为监听状态(128表示同时允许访问服务器的客户端个数，同一个数在不同的操作系统中允许的大小有差异)
    tcp_download_server.listen(128)
    while True:
        #   4.接收客户请求
        print("等待用户响应!!!")
        client_socket,client_addr=tcp_download_server.accept()
        server_to_client(client_socket)

    #   8.服务器关闭
    # tcp_download_server.close()

if __name__=="__main__":
    main()