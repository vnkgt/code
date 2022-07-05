#传参问题(传的参数个数不固定)
"""
    参数问题:
    1)直接传参与参数名传参
        eg:     def test(name):
                    print(name)
                test("laowang")   # 直接传参(位置参数)
                test(name = "laoli")  # 参数名传参(关键字参数)

    2)*args:传参时多余的，直接传参的，参数元组
      *kwargs:传参时多余的，参数名传参的，参数字典
      在函数内又可通过*和**来解包元组与字典。
      eg:
        def test2(*args,**kwargs):
            print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>test2")
            print(" *args={0} \n **kwargs={1}".format(args, kwargs))
        def test1(a,b,*args,**kwargs):
            print("-------------test1")
            print(" a={0} \n b={1} \n *args={2} \n **kwargs={3}".format(a, b, args, kwargs))

            # 解包传参
            test2(*args,**kwargs)

        test1(1,2,23,"fsd",p=90,ac="asd")

    3)特别注意:
        传参时参数除了可以是某个具体的对象外，还可以是指向函数的变量
        eg:
            def func1(arg):---->arg指向一个函数，可以是已经定义函数的名字
                arg()----------->调用arg指向的函数
            def func2():
                print("Hello Word!!!")
            func1(func1)


"""
#1.测试：参数解包
# def test2(*args,**kwargs):
#     print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>test2")
#     print(" *args={0} \n **kwargs={1}".format(args, kwargs))
#
#
# def test1(a,b,*args,**kwargs):
#     print("\n-------------test1")
#     print(" a={0} \n b={1} \n *args={2} \n **kwargs={3}".format(a, b, args, kwargs))
#
#     # 解包传参(相当于将arg元组的所有元素取出来再一个一个放入)
#     test2(*args,**kwargs)
#
# test1(1,2,23,"fsd",p=90,ac="asd")



#2.测试：传递函数指向
# def func(func_name,number):
#     func_name(number)    #调用func_name指向的函数
#
# def test(num):
#     print("Hello Word!!!----%s " % num)
#
# func(test,10)
# print(">"*20)
# temp = test       #temp指向test
# func(temp,20)

