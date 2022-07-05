#   多线程
"""
    线程与进程:
        进程：一个程序或软件运行起来后称为进程(程序与程序之间)
        线程：一个进程中包含一个或多个进程(程序内部)


    多线程:
        并行:cpu核心数>=线程个数
        并发:cpu核心数<线程个数
        一般为并发


    threading实现多线程:
        过程:1.threading.Thread(target=函数名)创建子线程对象---->2.start创建并运行子线程
        注意:
            1.主线程一定最后结束
            2.子线程在start时创建，并运行；在子线程函数代码结束时结束
            3.使用class封装子线程时一定要继承threading.Thread父类，class中一定要有run函数，
                当start调用封装子线程时会自动调用class中的run函数
            4.可以使用time.sleep()调整线程之间的先后顺序
            5.threading.enumerate()可以查看目前正在运行的线程个数
            6.threading.Thread(target=函数名，args=(参数元组))   使用args为函数传递参数
            7.多线程之间共享全局变量，但共享时可能会导致资源占用问题，可使用互斥锁解决，同一个互斥锁同一时刻只能锁一次
                mutex = threading.Lock()创建锁
                mutex.acquire()    锁死
                mutex.release()     解锁
                互斥锁使用时应当锁住尽量少的代码

"""
import threading,time,socket


"""1)实现一个普通的多线程"""


# def test1():
#     for i in range(2):
#         print("-----test1运行%d-------" % (i))
#         time.sleep(1)
#
#
# def test2():
#     for i in range(5):
#         print("cccccccccccccccc\ttest2正在运行%d" % (i))
#         time.sleep(1)
#
#
# def main():
#     #     创建线程对象
#     t1 = threading.Thread(target=test1)
#     t2 = threading.Thread(target=test2)
#
#
#     #     创建线程并运行
#     t1.start()
#     t2.start()
#
#     print(threading.enumerate())
#
# if __name__ == "__main__":
#     main()


"""2)time.sleep控制进程之间的先后关系"""


# def test1():
#     for i in range(4):
#         print("----------正在唱歌：" , i)
#         time.sleep(1)
#
#
# def test2():
#     for i in range(7):
#         print("+++++++++++正在喝茶:" , i)
#         time.sleep(1)
#
#
# def main():
#     #   创建线程对象
#     t1 = threading.Thread(target=test1)
#     t2 = threading.Thread(target=test2)
#
#     #   创建线程对象
#     t1.start()
#     time.sleep(1)
#     t2.start()
#
#
#
# if __name__ == "__main__":
#     main()


"""3)class封装子线程"""


# #   class封装后子线程的功能应在run函数中实现
# class MyThread(threading.Thread):
#     def run(self):
#         print("Hello word!!!")
#         self.test1()
#         self.test2()
#
#
#     def test1(self):
#         print("FUCK")
#
#
#     def test2(self):
#         print("YOU!!!")
#
#
# def main():
#     t = MyThread() # 创建封装的子线程对象
#     t.start()      # 运行子线程(自动运行run函数)
#
#
# if __name__ == "__main__":
#     main()


"""4)多线程函数传递参数"""


# def test1(num):
#     for i in range(10):
#         num += 1
#     print("test1:%d" % num)
#
#
# def test2(num):
#     for i in range(2):
#         num += 1
#     print("test2:%d" % num)
#
#
# def main():
#     """主线程"""
#     t1 = threading.Thread(target=test1,args=(0,))
#     t2 = threading.Thread(target=test2,args=(0,))
#
#     t1.start()
#     t2.start()
#
# if __name__ == "__main__":
#     main()


"""5)多线程共享全局变量"""


"""
    global说明:
        当全局变量指向的地址发生改变是需要global说明
        当全局变量指向的地址未发生改变是不需要global说明
"""
#   A.使用全局变量
# def test1():
#     global num
#     num += 1
#     print("test1:",num)
#
#
# def test2():
#     global num
#     num += 1
#     print("test2:",num)
#
# def  main():
#     """主线程"""
#     t1 = threading.Thread(target=test1)
#     t2 = threading.Thread(target=test2)
#
#     t1.start()
#     t2.start()
#
# num = 0
#
# if __name__ == "__main__":
#     main()

#   B.使用全局变量时的问题:资源占用
# def test1():
#     global num
#     for i in range(100000):
#         num += 1
#     print("test1:",num)
#
#
# def test2():
#     global num
#     for i in range(100000):
#         num += 1
#     print("\ntest2:",num)
#
#
# def main():
#     t1 = threading.Thread(target=test1)
#     t2 = threading.Thread(target=test2)
#
#     t1.start()
#     t2.start()
#
#     time.sleep(1)
#     print("MianThread:",num)
# # 全局变量
# num = 0
#
# if __name__ == "__main__":
#     main()

#   C.互斥锁解决
#   1.
# def test1(mutex):
#     global num
#     mutex.acquire()
#     for i in range(1000000):
#         num += 1
#     mutex.release()
#     print("test1:",num)
#
#
# def test2(mutex):
#     global num
#     mutex.acquire()
#     for i in range(1000000):
#         num += 1
#     mutex.release()
#     print("test2:",num)
#
#
# def main():
#     "主线程"
#     mutex = threading.Lock()  # 创建互斥锁
#
#     t1 = threading.Thread(target=test1,args=(mutex,))
#     t2 = threading.Thread(target=test2, args=(mutex,))
#
#     t1.start()
#     t2.start()
#
#     time.sleep(3)
#     print("MianThread:",num)
#
# num = 0
#
#
# if __name__ == "__main__":
#     main()

#   2.
# def test1(mutex):
#     global num
#     for i in range(1000000):
#         mutex.acquire()
#         num += 1
#         mutex.release()
#     print("test1:",num)
#
#
# def test2(mutex):
#     global num
#     for i in range(1000000):
#         mutex.acquire()
#         num += 1
#         mutex.release()
#     print("\ntest2:",num)
#
#
# def main():
#     "主线程"
#     mutex = threading.Lock()  # 创建互斥锁
#
#     t1 = threading.Thread(target=test1,args=(mutex,))
#     t2 = threading.Thread(target=test2, args=(mutex,))
#
#     t1.start()
#     t2.start()
#
#     time.sleep(3)
#     print("MianThread:",num)
#
# num = 0
#
#
# if __name__ == "__main__":
#     main()


"""多任务udp聊天器"""

def recv_msg(udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)


def send_msg(udp_socket,dest_ip,dest_port):
    while True:
        send_data = input("发送的信息:")
        udp_socket.sendto(send_data.encode("GBK"),(dest_ip,dest_port))


def main():
    #   1.创建udp套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #   2.绑定本地端口ip
    udp_socket.bind(("",4321))

    #   获取目标ip及端口
    dest_ip = input("输入目标ip:")
    dest_port = int(input("输入目标port:"))


    #   3.创建收发信息的进程并运行
    t_recv = threading.Thread(target=recv_msg,args=(udp_socket,))
    t_send = threading.Thread(target=send_msg, args=(udp_socket,dest_ip,dest_port))

    t_recv.start()
    t_send.start()
    #   4.关闭套接字

if __name__ == "__main__":
    main()