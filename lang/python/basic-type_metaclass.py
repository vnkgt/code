#type()
"""
1)type的作用:
    1.1.查看某个对象的类型
    1.2.动态创建类:
        type(类名，（父类元组可以为空），类属性字典)
        类属性字典：  key--->类内部对象的名称
                    value--->一个对象(可以是具体的字符串、数字、元组、列表、字典，也可以是函数的引用(函数名)，类对象的引用(类名))
        eg:
            test = type("test",(),{'id':12,'name':laowang})

2)元类(创建类对象的类):
    2.1.元类---->元类---->类对象---->实例对象
    2.2.继承type类的内对象是元类
            eg:class metaclass(type):---->元类对象
                    pass
    2.3.一般的类对象继承元类对象时会自动执行元类对象的__new__方法
            2.3.1.元类对象一般，使用__new__方法处理普通对象后，返回新的普通对象
            2.3.2.元类对象的__new__方法:  __new__(cls,name,base,attrs)
                    (可以对比:type(类名，（父类元组可以为空），类属性字典))
                    cls--->元类对象自己本身,当被其他对象继承时cls指向其他对象             bases--->传入普通类对象的父类对象
                    name--->传入普通类对象的类名                                      attrs--->传入普通对象的属性(包括函数方法)
    2.4.普通对象通过class 普通类名(metaclass=元类名)来继承元类对象
        普通对象在继承元类对象时会自动调用__new__方法并向其传递 自己类对象的指向、自己的类名、自己父类对象的元组、自己内部的所有的属性字典 这些基本参数
            ====>相当于 __new__(自己类对象的指向,自己的类名,自己父类对象的元组,自己内部的所有的属性字典)
    eg：
        class mc(type):                     ---->元类对象
            def __new__(...):
                ...
                return type.__new__(...)    ---->通过type返回经过修饰过的普通类对象
        class temp1(metaclass = mc):        ----->普通内对象继承mc元类对象
            pass

"""

#元类测试
class Temp_metaclass(type):   #    type为父类，该类为元类
    #   当其他对象继承该对象时，自动执行__new__(cls,*args,**kwargs)函数
    #   cls:指向类对象   base:继承父类对象     name:类名   attrs:属性字典
    def __new__(cls,name,base,attrs):  
        print("IN Temp_metaclass\n-->cls指向的类对象:{0}<-\n->继承的父类:{2}<-\n->属性字典:{3}<-\n->类名:{1}<--".format(cls,name,base,attrs))
        #   cls指向进来的类对想
        return type.__new__(cls,name,base,attrs) 
               
#   继承object对象,元类对象Temp_metaclass
#   继承时会自动向元类对象的__new__方法中传入自己类对象的指向、自己的类名、自己父类对象的元组、自己内部的所有的属性字典
class temp(object,metaclass=Temp_metaclass):    
    def __init__(self):
        self.id = 12
    def test(self):
        print("This is tempclass!!!")

t1 = temp() #该实例对象创建时会自动调用Temp_metaclass中的__new__方法
print("\n\n-----t1实例对象的id属性----->",t1.id)