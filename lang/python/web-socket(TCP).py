#   TCP客户端/服务器
"""
    TCP客户端流程:
        1.创建套接字---->2.链接服务器---->3.收发数据---->4.关闭套接字
    ip:地址   port:端口

    TCP的三次握手:
        客户端与服务器正式进行数据传输前，双方(客户端与服务器)进行资源的准备(connect)
    TCP的四次挥手:
        客户端与服务器断联时，双方(客户端与服务器)进行资源释放的确认，谁先调用close就谁先等待2-5分钟,等待期间会造成端口的占用，
        可以使用    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)实现端口重复使用来解决问题
        tcp_server_socket代表tcp服务器的套接字
"""
import socket


# def main():
#     #   创建套接字（socket.SOCK_STREAM为Tcp套接字）
#     tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
#     #   链接服务器
#     server_ip=input("服务器ip:")
#     server_port=int(input("服务器port:"))
#     tcp_socket.connect((server_ip,server_port))
#
#     #   数据发送
#     send_data=input("发送的数据:")
#     tcp_socket.send(send_data.encode("GBK"))
#
#     #   关闭套接字
#     tcp_socket.close()
#     print("Over!!!")
#
# if __name__=="__main__":
#     main()



"""
    TCP服务器:
        流程:1.创建监听套接字---->2.bild绑定本地信息---->3.listen等待客户端连接(将主动状态改为被动状态)---->4.accept接收客户端请求---->5.recv\send(为客户新建的套接字)收发信息
        工作原理:1.监听套接字:只负责接收客户端连接请求
                2.客户端链接后:会返回一个元组(创建一个新服务的套接字,(用户ip,用户port))
                3.创建新服务的套接字用于服务客户端收发信息
                4.每有一个客户端链接时都会创建一个新的服务套接字
                5.监听套接字相当于前台老板，服务套接字相当于前台服务员，老板分发任务，服务员实际服务客户
                6.套接字默认为主动状态：用于发送信息
                             被动状态：等待被连接
"""

def main():
    #   创建监听套接字（TCP套接字）
    tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #   绑定本地信息
    tcp_server_socket.bind(("192.168.0.104",9900))


    #   变为被动模式
    tcp_server_socket.listen()

    #   接收客户请求
    client1_socket,client1_addr=tcp_server_socket.accept()
    while True:
        #   接收客户发来的信息
        client1_data=client1_socket.recv(1024)

        #   判断客户端是否下线
        if client1_data:
            #   打印用户发送信息
            print("from{0}:".format(str(client1_addr)),client1_data.decode("GBK"))

            #   消息反馈（client1服务器反馈客户client1）
            client1_socket.send(b"FUCK YOU!!!")
        else:
            print("该客户已离线!!!")
            break
    #   关闭客户端套接字
    client1_socket.close()


    #   关闭服务器监听套接字
    print("服务器关闭!!!")
    tcp_server_socket.close()

if __name__=="__main__":
    main()

