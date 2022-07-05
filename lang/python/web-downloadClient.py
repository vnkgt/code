#   Tcp下载客户端
import socket
import time

def main():
    #   1.创建客户端下载套接字
    tcp_download_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #   2.链接服务器端口地址
    server_addr=("192.168.0.104",1551)
    tcp_download_client.connect(server_addr)

    #   3.下载请求
    request_filename=input("要下载服务器文件的文件名:")
    tcp_download_client.send(request_filename.encode("GBK"))
    time.sleep(1)

    #   4.服务器返回内容分析(以及文件写入)
    back_data=tcp_download_client.recv(1024*1024)
    print(back_data)
    if back_data:
        with open("temp\\new"+request_filename,"ab") as backfile:
            backfile.write(back_data)
            print("下载完成!!!")
    else:
        print("服务器回传信息有误!!!")

    #   5.客户端关闭
    tcp_download_client.close()

if __name__=="__main__":
    main()