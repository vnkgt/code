#   多进程
"""
    多进程：
        程序(.exe)文件---->运行(进程)---->主线程开始执行
        每个进程都会占用内存以及系统硬件资源，多进程通过浪费资源来提高程序代码效率，但进程数不宜过多否则会造成卡死等情况

    多进程(厨房)与多线程(厨师):
        多进程：多个厨房多个厨师(3个厨房3个厨师)
        多线程：一个厨房多个厨师(1个厨房3个厨师)
        每个进程至少有一个线程(主线程)

    多线程:
        1.son_process = multiprocessing.Process(target=函数名，args=(参数元组))    创建进程对象
        2.son_process.start()    开始执行进程
        3.进程间数据沟通:通过Queue队列(数据先进先出)
            qu = multiprocessing.Queue(num)    创建队列  (num：队列最多的数据个数可有可无；无num时默认是最大值(最大值根据电脑而定))
            qu.put()                            队列中放数据
            qu.get()                            取出队列中的数据
            qu.full()                            判断队列数据是否已满
            qu.empty()                          判断队列中的数据是否为空
        4.控制同一时间时的进程个数:进程池(可向进程池当中放入许多个进程，进程池会会控制同一时刻的进程个数)
            po = multiprocessing.Pool(num)          创建进程个数为num个的进程池
            po.apply_async(func=函数名，args=(参数元组))        向进程池当中放进程
            po.close()                              关闭进程池，不再向进程池当中放进程
            po.join()                               等待进程池内的进程全部结束(须放在close之后)

补充:
    os.getpid() 获取进程id
    强制结束指定pidnum的进程:
        windows:os.system("taskkill /pid pidnum  -t  -f")
        linux:  os.system("kill pidnum")
"""
import multiprocessing,time,os




"""1）多进程的创建以及运行"""
# def test1(num):
#     print(num+1)
#
#
# def test2():
#     print("Hello word!!!")
#
#
# def main():
#     "创建多进程程"
#     p1 = multiprocessing.Process(target=test1,args=(1,))
#     p2 = multiprocessing.Process(target=test2)
#
#     p1.start()
#     p2.start()
#
#     time.sleep(1.5)
#     print("Over!!!")
#
#
# if __name__ == "__main__":
#     main()




"""2)进程间通过队列传递数据"""

# def test1(qu):
#     qu.put(10)
#     qu.put("sdfaljf")
#     qu.put([(12, "sd"), {"a": "asd", "sa": 231}], block=True, timeout=0.1)
#
#
# def test2(qu):
#     for i in range(3):
#         print(qu.get())
#
# def main():
#     #   创建队列，队列中最多有2个数据
#     qu = multiprocessing.Queue()
#     p1 = multiprocessing.Process(target=test1,args=(qu,))
#     p2 = multiprocessing.Process(target=test2, args=(qu,))
#
#     p1.start()
#     p2.start()
#     time.sleep(2)
#     print("Over!!!")
#
#
# if __name__ == "__main__":
#     main()


"""3)Pool控制同一时间的进程个数"""

# def test(num):
#     print("正在执行:",num)
#
# def main():
#     po = multiprocessing.Pool(3)
#     for i in range(10):
#         po.apply_async(func=test,args=(i,))
#
#     po.close()     # 关闭进程池
#     po.join()      # 等待进程池中的进程结束
#
#     print("Over!!!")
#
#
# if __name__ == "__main__":
#     main()


"""多进程文件拷贝器"""

def copy_file(filename,old_folder,new_folder,queue):
    # 读取老文件的内容
    read_file = open(old_folder+"/"+filename,"br")
    read_data = read_file.read()

    # 在新文件夹中创建一个新的同名文件
    write_file = open(new_folder+"/"+filename,"bw")
    write_file.write(read_data)

    queue.put(filename)



def main():
    # 获取要拷贝的文件夹命
    old_folder_name = input("输入要拷贝的文件夹命:")

    # 创建新的文件夹
    try:
        new_folder_name = old_folder_name+"[复件]"
        os.mkdir(new_folder_name)
    except:
        pass

    # 获取老文件夹中的文件
    file_names = os.listdir(old_folder_name)

    # 拷贝
        # pool控制进程个数
    pool = multiprocessing.Pool(4)
        # queue传递参数，显示进度条
    queue = multiprocessing.Manager().Queue()
        # 进程池当中添加进程
    for filename in file_names:
        pool.apply_async(func=copy_file,args=(filename,old_folder_name,new_folder_name,queue))

    # 显示进度条
    speed_num = 0
    while True:
        filename_over = queue.get()
        speed_num+=1
        percent = (speed_num*100)/len(file_names)
        print("\r"+filename_over+"\tpercent:%0.2f %%" % (percent))
        if speed_num>=len(file_names):
            print("Over!!!")
            break


if __name__ == "__main__":
    main()