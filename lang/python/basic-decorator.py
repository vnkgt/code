#修饰器
"""
装饰器:
    修饰的实现方法:
        实参传指向函数的变量(见parameter) + 闭包(见closure)

    1.一般方法:
        def decorator(func_name_pointer):             ----->func_name_pointer为指向一个函数的变量(包括直接写函数名)
            def dec_func(dec_func参数):
                dec_func函数的内容
                func_name_pointer(要传给指定函数的参数)----->调用func_name_pointer指向的函数并传参
            return dec_func                           ----->调用闭包内部的dec_func函数
        @decorator                                    ----->使用decorator修饰test函数
        def test(test参数):
            test函数的内容
        test(实参)                                    ---->调用经decorator函数修饰过后的test函数

        辅助理解,以上代码相当于以下两端代码(传递相同的参数时1)和2)的结果一样):
            1)
                def decorator(func_name):
                    def dec_func(num):
                        print("----这是验证权限-----")
                        func_name(num)
                    return dec_func
                def test(n):
                    print("Hello Word!!!---%s" % n)
                decorator(test)(10)                 ---->decorator(test)指向test函数
            2)
                def decorator():
                    def dec_func(number):
                        print("-----这是验证权限-----")
                        def test(num):
                            print("Hello Word!!!----%s" % num)
                        return test(number)
                    return dec_func
                decorator()(10)

    2.万能修饰器（返回调用的函数、可以传不定数目的参数）:
        写法:
            def decorator(func_name_pointer):
                def dec_func(*args,**kwargs):               ----->传参时可以接收任意数目的参数
                    语句
                    return func_name_pointer(*args,**kwargs)  ----->解包参数并返回被修饰函数的调用
                return dec_func
            说明:（详情见2parameter.py文件）
                def dec_func(*args,**kwargs)    *args:存放直接传参的参数(返回一个元组)  **kwargs:存放函数名传参的参数(返回一个字典)
                return func_name_pointer(*args,**kwargs)  *args、**kwargs:将元组拆分为一个个单独的参数

    3.带参数的修饰器:
        写法:
            def get_decorator_arg(decorator_arg):----->用来接收修饰器的参数
                def decorator(func_name_pointer):----->修饰器的主体函数
                    def dec_func():
                        语句
                        func_name_pointer()     ------>调用被修饰的函数
                    return dec_func
                return decorator                ----->返回修饰器

            @get_decorator_arg(修饰器的参数)     ----->使用带参数的修饰器
            def func():                         ------>被修饰的函数
                pass
            func()                              ----->使用func函数

    4.带参数的万能(通用)修饰器:万能修饰器 + 带参数的修饰器
        写法:
            def get_decorator_arg(decorator_arg):
                def decorator(func_name_pointer):
                    def dec_func(*args,**kwargs):
                        语句
                        return func_name_pointer(*args,**kwargs)
                    return dec_func
                return decorator

            @get_decorator_arg(修饰器变量)
            def ordinary_func(*args,**kwargs):
                语句

            ordinary_func(参数)


"""

"""1)装饰器的简单测试"""
#装饰器测试代码
def decorator(func_name_pointer):
    def dec_func(number):
        print("-------这是权限验证------")
        func_name_pointer(number)
    return dec_func

@decorator
def test(n):
    print("Hello word!!!---- %s " % n)

test(1110)  # 调用



#辅组理解代码1
def decorator():
    def dec_func(number):
        print("-----这是验证权限-----")
        def test(num):
            print("Hello Word!!!----%s" % num)
        return test(number)             #调用内部的test函数
    return dec_func                     #调用内部的dec_func函数

decorator()(10)



#辅助理解代码2
def decorator(func_name):
    def dec_func(num):
        print("----这是验证权限-----")
        func_name(num)
    return dec_func         #调用内部的dec_func函数

def test(n):
    print("Hello Word!!!---%s" % n)

decorator(test)(20)


"""2)使用装饰器实现，函数运行时间计时器"""
import time
def time_geter(func_name_pointer):
    def dec_func():
        start_time = time.time()
        func_name_pointer()
        end_time = time.time()
        print("函数{0}共用时:{1}".format(func_name_pointer,end_time-start_time))
    return dec_func

@time_geter
def test1():
    for i in range(1000):
        pass

@time_geter
def test2():
    for i in range(100000):
        pass

test1()
test2()


"""3)多个修饰器修饰一个函数后调用先后顺序"""
def decorator1(func_name_pointer1):
    def dec1_func():
        print("这是decorator  1")
        func_name_pointer1()
    return dec1_func

def decorator2(func_name_pointer2):
    def dec1_func():
        print("这是decorator  2")
        func_name_pointer2()
    return dec1_func

@decorator1
@decorator2
def test1():
    print("test   1")

@decorator2
@decorator1
def test2():
    print("test   2")

@decorator1
@decorator2
@decorator1
@decorator2
def test3():
    print("test   3")

test1()
test2()
test3()


"""4)多个修饰器修饰函数时修饰的先后顺序"""
def decorator1(func_name_pointer):
    print("----------->修饰器  1正在修饰<--------------")
    def dec_func(*args,**kwargs):
        return func_name_pointer(*args,**kwargs)
    return dec_func

def decorator2(func_name_pointer):
    print("----------->修饰器  2正在修饰<--------------")
    def dec_func(*args,**kwargs):
        return func_name_pointer(*args,**kwargs)
    return dec_func

@decorator1
@decorator2
def test1():
    print("test1")


"""5)带参数的修饰器"""
def get_decorator_arg(num1,num2):
    def decorator(func_name_pointer):
        def dec_func(*args,**kwargs):
            print("修饰器的参数:num1:{0}\tnum2:{1}".format(num1,num2))
            return func_name_pointer(num1,num2)
        return dec_func
    return decorator

@get_decorator_arg(99,77)
def test(*args):
    print("test")
    print(args)

test()
