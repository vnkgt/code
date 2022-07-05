#   协程
"""
    1.可迭代对象(迭代器)：1)可使用isinstance(要判断的对象,Iterable)判断是否为可迭代对象
                            Iterable:导入方法  from collections import Iterable
                       2)可使用iter(可迭代对象)生成一个可迭代对象得到__iter__的返回值，
                       可使用iter(可迭代对象).__next__()查看返回(迭代对象)值的__next__()方法
                            #   可迭代对象(必须含有__iter__方法)                  #    可迭代对象的返回值--迭代器(必须含有__iter__和__next__方法)
                            class Iterable(object):                             class IterableReturn(object):
                                def __iter__(self):       --------->                def __iter__(self):
                                    pass                                                pass
                                                                                    def __next__(self):
                                                                                        pass
                             使用：(for temp in 可迭代对象:)时会自动调用__iter__的返回值和__next__方法
                       3)一个迭代器对象只能使用遍历一次


    2。生成器:一种特殊的迭代器
            1)创建方法:A.通过小括号()实现     B.通过yield实现
            2)yield使用方法:
                            def  函数X():
                                .....
                                while True:
                                    ret = yield something
                                return returnvalue

            yield的值传出生成器:   ret = 函数X()    ret的值为something

            生成器启动:
                A方法:                            B方法:(该方法相当于把send中的参数传给yield运行的生成器内部结果)
                    next(生成器)                       生成器.send(args)
                                                       使用该方法启动时第一次时用可能会报错，可以用send(None)解决
                eg:A = 函数X()                    A = 函数X()
                   result = next(A)               A.send("FUCK!!!")

            生成器的return值可使用：    value实现外传
                eg:A = 函数X()
                   returnResult = A.value()

            总结：yieldvalue = 生成器()  (生成器内部:ret = yield something)
                  生成器内部==>外部:   yieldvalue的值是something
                  外部==>生成器内部:   yieldvalue.send(args)  相当于把args传给ret
           3)当函数内部有yield时不再称为函数，称为生成器
           4)没有使用next()或send()启动时，生成器内部的代码不会运行；
             每调用一次next()或send()时会将yield的值返回并暂停，下次再调用时从yield暂停的地方向下执行；
             生成器结束：生成器内部的代码结束.
           5)运行到yield时相当于暂停并向外传值


    3.协程:(迭代器+多线程)
        实现方法:
        1)yield(了解)
        2)greenlet(第三方模块):(了解)
            创建方法: gr = greenlet.greenlet(函数名)    自动将函数迭代化
            转换到某个线程的方法:   gr1.switch()      转到gr1的代码
                                    gr2.switch()     转到gr2的代码
        3)gevent(第三方模块):
            创建方法:   ge = gevent.spawn(函数名)          自动将函数迭代化
            开始方法:   ge.join()           等待ge结束
                        gevent.joinall([gevent.spawn生成对象的列表])    自动管理并等待所有的对象代码结束
            注意点: 使用延时方法时需要替换为gevent.xxxxx    eg:time.sleep(1)------>gevent.sleep(1);
                    或打补丁添加monkey.patch_all()自动将代码中的延时操作替换为gevent.xxxxx
                    monkey导入方法from gevent import monkey
            当gevent遇到延时操作时会自动切换代码

"""
from collections import Iterable
import time


"""1)可迭代对象的测试"""


# A.简单测试

# def main():
#     class ItorReturn(object):
#         def __init__(self):
#             pass
#         def __iter__(self):
#             pass
#         def __next__(self):
#             print("FUCK!!!")
#
#
#     class Itor(object):
#         def __init__(self):
#             pass
#         def __iter__(self):
#             return ItorReturn()
#
#     print("Iterabler()是否为可迭代对象:",isinstance(Itor(),Iterable))
#     A = iter(Itor())
#     print("可迭代对象的__next__():A.__next__():")
#     A.__next__()
#     print("or next(A):")
#     next(A)
#     print("A是否为可迭代对象:",isinstance(A,Iterable))
#
# if __name__ == "__main__":
#     main()

# B.可迭代对象测试列表的for打印
# def main():
#     class ClassmateItor(object):
#         def __init__(self,obj):
#             self.obj = obj
#             self.counter = 0
#         def __iter__(self):
#             pass
#         def __next__(self):
#             # 小于names列表的长度
#             if self.counter<len(self.obj.namelist):
#                 self.counter+=1
#                 return self.obj.namelist[self.counter-1]
#             # 其余报错停止打印
#             else:
#                 raise StopIteration
#
#
#     class Classmate(object):
#         def __init__(self):
#             self.namelist = list()
#         def __iter__(self):
#             return ClassmateItor(self)
#
#     cl = Classmate()
#     cl.namelist.append("老王")
#     cl.namelist.append("老李")
#     cl.namelist.append("老张")
#
#     for i in cl:
#         print(i)
#         time.sleep(1)
#
# if __name__ == "__main__":
#     main()

# C.迭代器测试改良版
# def main():
#     class Classmate(object):
#         def __init__(self):
#             self.namelist = list()
#             self.count = 0
#         def __iter__(self):
#             return self
#         def __next__(self):
#             if self.count<len(self.namelist):
#                 self.count += 1
#                 return self.namelist[self.count-1]
#             else:
#                 raise StopIteration
#
#     cl = Classmate()
#     cl.namelist.append("老王")
#     cl.namelist.append("老李")
#     cl.namelist.append("老张")
#
#     for i in cl:
#         print(i)
#         time.sleep(1)
#
# if __name__ == "__main__":
#     main()

# D.迭代器实现斐波拉契数列
# def main():
#     class Fibonacci(object):
#         def __init__(self,all_count):
#             # 属性
#             self.num1 = 0
#             self.num2 = 1
#             self.all_count = all_count
#             self.temp_count = 0
#         def __iter__(self):
#             # 返回自身调用
#             return self
#         def __next__(self):
#             if self.temp_count<self.all_count:
#                 ret = self.num1
#                 self.num1, self.num2 = self.num2, self.num1 + self.num2
#                 self.temp_count += 1
#                 return ret
#             else:
#                     # 抛出异常结束
#                     raise StopIteration
#
#     fo = Fibonacci(10)
#     print(fo)
#     for i in fo:
#         print(i)
#
#
# if __name__ == "__main__":
#     main()



"""2)生成器"""


# A.使用生成器实现斐波拉契数列(next())
# def main():
#     def fibonacci(all_count):
#         num1, num2 = 0, 1
#         in_count = 0
#         while True:
#             yield num1
#             num1, num2 = num2, num1+num2
#             in_count += 1
#             if in_count>=all_count:
#                 break
#
#     fo = fibonacci(10)
#
#     print("planA:")
#     for i in range(10):
#         ret = next(fo)
#         print(ret)
#
# if __name__ == "__main__":
#     main()

# B.生成器send使用测试(生成器内return值测试)
# def main():
#     def fibonacci(all_count):
#         num1, num2 = 0, 1
#         in_count = 0
#         while True:
#             ret = yield num1
#             num1, num2 = num2, num1+num2
#             in_count += 1
#             print("------------->>>>ret:",ret)
#             if in_count>=all_count:
#                 break
#         return "FUCK!!!"
#
#     # return返回值测试
#     print("return测试:")
#     fo = fibonacci(0)
#     try:
#         while True:
#             retresult = next(fo)
#             print("retresult:",retresult)
#     except Exception as overReturn:
#         print(overReturn.value)
#
#     # send测试
#     print("\n\n\nsend测试:")
#     fo = fibonacci(10)
#     for i in range(10):
#         if i == 0:
#             result = fo.send(None)
#         else:
#             result = fo.send(chr(i*20))
#         print("yield返回值:",result)
#
#
# if __name__ == "__main__":
#     main()


"""3)协程"""
import greenlet
import gevent

# A.yield实现协程
# def creater(name):
#     count = 0
#     while True:
#         print("-------"+str(name))
#         count += 1
#         time.sleep(1)
#         # 相当于暂停
#         yield
#
# def main():
#     cr1 = creater("A")
#     cr2 = creater("B")
#     while True:
#         next(cr1)
#         next(cr2)
#
#
# if __name__ == "__main__":
#     main()

# B.greenlet实现协程(test1->test2->test1->test2.......)
# def main():
#     def test1():
#         while True:
#             print(">>>>>>>>>>A")
#             # 跳到另一个greenlet.greenlet创建的生成器对象的代码当中
#             gr2.switch()
#             time.sleep(1)
#
#     def test2():
#         while True:
#             print(">>>>>>>>>>B")
#             # 跳到另一个greenlet.greenlet创建的生成器对象的代码当中
#             gr1.switch()
#             time.sleep(1)
#
#     gr1 = greenlet.greenlet(test1)
#     gr2 = greenlet.greenlet(test2)
#     gr1.switch()
#
# if __name__ == "__main__":
#     main()

# C.gevent实现协程(所有的延时操作要使用gevent.xxxxx  eg:gevent.sleep(1) )
# def test1():
#     while True:
#         print(".................A")
#         gevent.sleep(1)
#
#
# def test2():
#     while True:
#         print(">>>>>>>>>B")
#         gevent.sleep(1)
#
#
# def main():
#     #将函数可迭代化
#     ge1 = gevent.spawn(test1)
#     ge2 = gevent.spawn(test2)
#     # 等待结束
#     ge1.join()
#     ge2.join()
#
# if __name__ == "__main__":
#     main()

# D.通过monkey方法自动将代码中所有的延时操作转换为gevent.xxxx (eg:time.sleep(1)----->gevent.sleep(1))
# from gevent import monkey
# # 打monkey补丁自动替换延时操作
# monkey.patch_all()
#
# def test1():
#     while True:
#         print("------------------A")
#         time.sleep(1)
#
#
# def test2():
#     while True:
#         print(">>>>>>>>>>>>>>B")
#         time.sleep(1)
#
#
# def main():
#     ge1 = gevent.spawn(test1)
#     ge2 = gevent.spawn(test2)
#     # 可使用gevent.joinall([gevent.spawn对象列表])自动管理，并等待结束
#     gevent.joinall([ge1,
#                     ge2])
#
# if __name__ == "__main__":
#     main()

# E.图片下载器(协程下载)
# import urllib.request
# def img_downloader(img_url,local_name):
#     with open("E:/tempimg/"+local_name,"ba") as f:
#         img = img_url.read()
#         f.write(img)
#         print("已完成:",local_name)
#
# def main():
#     img_url_list = ["https://dss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2645905318,2571681756&fm=111&gp=0.jpg",
#                     "https://dss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=4193307353,2982239201&fm=111&gp=0.jpg",
#                     "https://dss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2999868051,3803578296&fm=111&gp=0.jpg",
#                     "https://dss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3452018725,200709180&fm=26&gp=0.jpg",
#                     "https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=1608685314,3739075620&fm=11&gp=0.jpg"]
#     counter = 0
#     gevent_obj_list = list()
#     for i in img_url_list:
#         #获取图片的url
#         req = urllib.request.urlopen(i)
#         #添加协程对象
#         gevent_obj_list.append(gevent.spawn(img_downloader(req,str(counter)+".jpg")))
#         counter += 1
#     # 开始协程
#     gevent.joinall(gevent_obj_list)
#
# if __name__ == "__main__":
#     main()