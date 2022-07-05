#   socket完成UDP收发数据

"""
ip:电脑地址    port:程序端口
流程：    1）发送数据:创建套接字---->发送(数据编码)---->关闭
                    (打开文件)---->(文件写入)---->(文件关闭)
         2)接收数据:创建套接字---->地址绑定(ip和port)---->数据接收(并解码)---->关闭
"""
import socket
"""
    1)发送数据
"""
# def main():
#     information=b"FUCK"           #  发送的信息
#     add=("192.168.147.129",8080)        #   地址元组(IP地址,port端口地址)
#
#     #   创建UDP套接字  AddressFamily:socket.AF_INET(用于Internet进程间通信)     Type:socket.SOCK_DGRAM(套接字类型UDP、TCP等)
#     udp_scoket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#
#     #   数据发送
#     udp_scoket.sendto(information,add)
#     print("正在运行!!!")
#
#     #   关闭
#     udp_scoket.close()
#     print("运行结束!!!")
#
#
# if __name__=="__main__":
#     main()

"""
    2)循环发送数据
"""

# def main():
#     # 创建udp套接字
#     udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#     # 循环发送信息
#     while True:
#         data = input("输入:")
#         if data=="exit":
#             break
#         udp_socket.sendto(data.encode("GBK"),("192.168.147.129",8080))   # data.encode("utf-8")将数据编码为utf-8
#     # 关闭
#     udp_socket.close()
#     print("Over!!!")
#
# if __name__=="__main__":
#     main()

"""
    3)数据接收
"""
# def main():
#     #创建udp套接字
#     udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#     # 端口绑定(ip可以不写，ip必须是本机ip,本机ip可通过ipconfig(windows)或ifconfig(linux)查看)
#     myaddr=("",6677)
#     udp_socket.bind(myaddr)
#     # 数据接收(并解码)
#     rev=udp_socket.recvfrom(1024) # 1024:每次接收数据的最大值
#     rev_data=rev[0]         # 接收的数据
#     rev_addr=rev[1]         # 接收数据的地址
#     # 数据打印
#     print("%s:%s"%(str(rev_addr),str(rev_data.decode("GBK"))))
#     #   关闭
#     udp_socket.close()
#
# if __name__=="__main__":
#     main()

"""
    4)循环接收信息
"""
# def main():
#     # 创建套接字
#     udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#     #  端口绑定
#     myaddr=("",6677)
#     udp_socket.bind(myaddr)
#     #   数据循环接收
#     while True:
#         rev=udp_socket.recvfrom(1024)
#         rev_data=rev[0]
#         rev_addr=rev[1]
#         print("%s:%s"%(str(rev_addr),str(rev_data.decode("GBK"))))
#     #   关闭
#     udp_socket.close()
#     print("Over!!!")
#
# if __name__=="__main__":
#     main()


"""
    5)循环接收发送数据
"""
def send_msg(udp_socket,addr):
    """数据发送函数"""
    send_data=input("发送数据")
    udp_socket.sendto(send_data.encode("GBK"),addr)


def recv_msg(udp_socket):
    """数据接收函数"""
    recv_data=udp_socket.recvfrom(1024)
    print("%s:%s" % (recv_data[1],recv_data[0].decode("GBK")))

def main():
    # 创建udp套接字
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #  (本地)端口绑定
    local_addr=('',7788)
    udp_socket.bind(local_addr)

    # 目标地址获取
    destination_ip = input("目标ip：")
    destination_port = int(input("目标port:"))
    destination_addr=(destination_ip,destination_port)


    # 循环接收发送数据
    while True:
        print("1:发送数据")
        print("2:接收数据")
        print("0:退出")
        optionflag=input("输入操作选项:")
        if optionflag=="1":
            send_msg(udp_socket,destination_addr)
        elif optionflag=="2":
            recv_msg(udp_socket)
        elif optionflag=="0":
            break
        else:
            print("输入有误重新输入")


if __name__=="__main__":
    main()