#类class
"""
类（封装、继承、多态）：
    1.私有化:
        xxx: 共有变量
        _xxx:  from kkk import * 禁止导入xxx
        __xxx:  私有属性，无法在外部直接访问
        __xxx__: 魔法方法或属性，继承时可以被继承。如:__init__
        xxx_: 无特殊含义，但可以在命名时解决命名冲突。
                eg:已命名:name 想在命名一个为name的变量，则可以命名为name_,从而解决冲突。


    2.多继承问题:
        前提:class 类名(父类名列表):      class已经继承了父类

        继承方法（在class的__init__方法中）:
            1)父类名.__init__(参数)
            2)super().__init__(参数)
            3)super(父类名,self).__init__(参数)

        super(类名).__init__(参数)功能的实现:
        A.MRO
            内存中有MRO(继承顺序表)，不同的class的MRO可能会有所差异
            MRO可通过:类对象.__mro__()进行查看
        B.super(类名).__init__(参数)
            super(类名).__init__(参数)函数会拿着 "类名" 在MRO中进行匹配，匹配到 则继承 该类的下一个类
        C.super().__init__(参数)
            默认类名为自己
            eg:
                MRO为<"class A","class B","class C","class object">
                继承顺序:A-->B-->C-->object
                        A继承B,B继承C,C继承object
                class K(A):
                    def __init__(参数):
                        # 继承class C的属性和方法
                        super(B,self).__init__(参数)


    3.property属性的实现:
        1)通过property(fget=None, fset=None, fdel=None, doc=None)函数实现
        参数说明:
            fget:   方法名，调用 对象.属性 时自动触发执行方法
            fset:   方法名，调用 对象.属性 ＝ XXX 时自动触发执行方法
            fdel:   方法名，调用 del 对象.属性 时自动触发执行方法
            doc:    字符串，调用 对象.属性.__doc__ ，此参数是该属性的描述信息
        2)通过@property装饰器实现
            @property                    @func.setter                       @func.deleter
            def func(self):               def func(self,value):             def func(self):
                xxxx                            xxxx                            xxx
                return  xxx                     return xxx                      del xxx
            对象.func---->自动调用@property下的方法，该方法需要有返回值
            对象.func = value---->自动调用@func.setter下的方法
            del 对象.func---->自动调用@func.deleter下的方法
        eg:
        方法2）
        class Goods(object):
            def __init__(self):
                self.__money = 100

            def getprice(self):
                return self.__money

            def setprice(self,value):
                self.__money = value
                return self.__money

            def delprice(self):
                del self.__money
                print("Delete Finished!!!")


            price = property(getprice,setprice,delprice,"None...")

        obj = Goods()   # 创建Goods对象，自动调用__init__方法
        print(obj.price) # 打印price属性，obj.price 自动调用getprice方法
        obj.price = 200  # 修改price属性，obj.price = 200 自动调用setprice方法
        print(obj.price)
        del obj.price    # 删除price属性，自动调用 delprice方法

        方法1）
        class Goods(object):
            def __init__(self):
                self.__money = 100

            @property
            def price(self):
                return self.__money

            @price.setter
            def price(self,value):
                self.__money = value
                return self.__money

            @price.deleter
            def price(self):
                del self.__money
                print("Delete Finished!!!")

        obj = Goods()   # 创建Goods对象，自动调用__init__方法
        print(obj.price) # 打印price属性，自动调用@property下的方法
        obj.price = 200  # 修改price属性，自动调用@price.setter方法
        print(obj.price)
        del obj.price    # 删除price属性，自动调用@price.deleter方法


    4.魔法方法:
        基础魔法方法（较为常用）
                                    1.实例化对象时第一个被调用的方法
            __new__(cls[, ...])     2.其参数直接传递给__init__方法处理
                                    3.我们一般不会重写该方法
            __init__(self[, ...])	构造方法，初始化类的时候被调用
            __del__(self)	析构方法，当实例化对象被彻底销毁时被调用（实例化对象的所有指针都被销毁时被调用）
            __call__(self[, args...])	允许一个类的实例像函数一样被调用：x(a, b) 调用 x.__call__(a, b)
            __len__(self)	定义当被 len() 调用时的行为
            __repr__(self)	定义当被 repr() 调用时的行为
            __str__(self)	定义当被 str() 调用时的行为
            __bytes__(self)	定义当被 bytes() 调用时的行为
            __hash__(self)	定义当被 hash() 调用时的行为
            __bool__(self)	定义当被 bool() 调用时的行为，应该返回 True 或 False
            __format__(self, format_spec)	定义当被 format() 调用时的行为
    属性相关的方法
            __getattr__(self, name)	定义当用户试图获取一个不存在的属性时的行为
            __getattribute__(self, name)	定义当该类的属性被访问时的行为
            __setattr__(self, name, value)	定义当一个属性被设置时的行为
            __delattr__(self, name)	定义当一个属性被删除时的行为
            __dir__(self)	定义当 dir() 被调用时的行为
            __get__(self, instance, owner)	定义当描述符的值被取得时的行为
            __set__(self, instance, value)	定义当描述符的值被改变时的行为
            __delete__(self, instance)	定义当描述符的值被删除时的行为
    比较操作符
            __lt__(self, other)	定义小于号的行为：x < y 调用 x.__lt__(y)
            __le__(self, other)	定义小于等于号的行为：x <= y 调用 x.__le__(y)
            __eq__(self, other)	定义等于号的行为：x == y 调用 x.__eq__(y)
            __ne__(self, other)	定义不等号的行为：x != y 调用 x.__ne__(y)
            __gt__(self, other)	定义大于号的行为：x > y 调用 x.__gt__(y)
            __ge__(self, other)	定义大于等于号的行为：x >= y 调用 x.__ge__(y)
    算数运算符
            __add__(self, other)	定义加法的行为：+
            __sub__(self, other)	定义减法的行为：-
            __mul__(self, other)	定义乘法的行为：*
            __truediv__(self, other)	定义真除法的行为：/
            __floordiv__(self, other)	定义整数除法的行为：//
            __mod__(self, other)	定义取模算法的行为：%
            __divmod__(self, other)	定义当被 divmod() 调用时的行为
            __pow__(self, other[, modulo])	定义当被 power() 调用或 ** 运算时的行为
            __lshift__(self, other)	定义按位左移位的行为：<<
            __rshift__(self, other)	定义按位右移位的行为：>>
            __and__(self, other)	定义按位与操作的行为：&
            __xor__(self, other)	定义按位异或操作的行为：^
            __or__(self, other)	定义按位或操作的行为：|
    反运算（类似于运算方法）
            __radd__(self, other)	当被运算对象（左边的操作对象）不支持该运算时被调用
            __rsub__(self, other)	当被运算对象（左边的操作对象）不支持该运算时被调用
            __rmul__(self, other)	当被运算对象（左边的操作对象）不支持该运算时被调用
            __rtruediv__(self, other)	当被运算对象（左边的操作对象）不支持该运算时被调用
            __rfloordiv__(self, other)	当被运算对象（左边的操作对象）不支持该运算时被调用
            __rmod__(self, other)	当被运算对象（左边的操作对象）不支持该运算时被调用
            __rdivmod__(self, other)	当被运算对象（左边的操作对象）不支持该运算时被调用
            __rpow__(self, other)	当被运算对象（左边的操作对象）不支持该运算时被调用
            __rlshift__(self, other)	当被运算对象（左边的操作对象）不支持该运算时被调用
            __rrshift__(self, other)	当被运算对象（左边的操作对象）不支持该运算时被调用
            __rxor__(self, other)	当被运算对象（左边的操作对象）不支持该运算时被调用
            __ror__(self, other)	当被运算对象（左边的操作对象）不支持该运算时被调用
    增量赋值运算
            __iadd__(self, other)	定义赋值加法的行为：+=
            __isub__(self, other)	定义赋值减法的行为：-=
            __imul__(self, other)	定义赋值乘法的行为：*=
            __itruediv__(self, other)	定义赋值真除法的行为：/=
            __ifloordiv__(self, other)	定义赋值整数除法的行为：//=
            __imod__(self, other)	定义赋值取模算法的行为：%=
            __ipow__(self, other[, modulo])	定义赋值幂运算的行为：**=
            __ilshift__(self, other)	定义赋值按位左移位的行为：<<=
            __irshift__(self, other)	定义赋值按位右移位的行为：>>=
            __iand__(self, other)	定义赋值按位与操作的行为：&=
            __ixor__(self, other)	定义赋值按位异或操作的行为：^=
            __ior__(self, other)	定义赋值按位或操作的行为：|=
    一元操作符
            __neg__(self)	定义正号的行为：+x
            __pos__(self)	定义负号的行为：-x
            __abs__(self)	定义当被 abs() 调用时的行为
            __invert__(self)	定义按位求反的行为：~x
    类型转换
            __complex__(self)	定义当被 complex() 调用时的行为（需要返回恰当的值）
            __int__(self)	    定义当被 int() 调用时的行为（需要返回恰当的值）
            __float__(self)	    定义当被 float() 调用时的行为（需要返回恰当的值）
            __round__(self[, n])	定义当被 round() 调用时的行为（需要返回恰当的值）
            	                    1. 当对象是被应用在切片表达式中时，实现整形强制转换
            __index__(self)         2. 如果你定义了一个可能在切片时用到的定制的数值型,你应该定义 __index__
                                    3. 如果 __index__ 被定义，则 __int__ 也需要被定义，且返回相同的值
    上下文管理（with 语句）
            __enter__(self)	1. 定义当使用 with 语句时的初始化行为
                            2. __enter__ 的返回值被 with 语句的目标或者 as 后的名字绑定
            __exit__(self, exc_type, exc_value, traceback)	1. 定义当一个代码块被执行或者终止后上下文管理器应该做什么
                                                            2. 一般被用来处理异常，清除工作或者做一些代码块执行完毕之后的日常工作
    容器类型（一般用于操作容器类）
            __len__(self)	定义当被 len() 调用时的行为（一般返回容器类的长度）
            __getitem__(self, key)	定义获取容器中指定元素的行为，相当于 self[key]
            __setitem__(self, key, value)	定义设置容器中指定元素的行为，相当于 self[key] = value
            __delitem__(self, key)	定义删除容器中指定元素的行为，相当于 del self[key]
            __iter__(self)	定义当迭代容器中的元素的行为
            __reversed__(self)	定义当被 reversed() 调用时的行为
            __contains__(self, item)	定义当使用成员测试运算符（in 或 not in）时的行为

    5.在子类中调用父类的方法（通过super()函数实现）
        调用方法：(一般使用方法一)
            1)父类名.父类方法(参数)
            2)super().父类方法名(参数)---->super中不写参数


"""

# 商品对象
class Goods(object):
    def __init__(self):
        self.__money = 100

    def getprice(self):     # 获取价格
        return self.__money

    def setprice(self,value):   # 修改价格
        self.__money = value
        return self.__money

    def delprice(self):     # 删除价格
        del self.__money
        print("Delete Finished!!!")


    price = property(getprice,setprice,delprice,"None...")

obj = Goods()   # 创建Goods对象，自动调用__init__方法
print(obj.price) # 打印price属性，obj.price 自动调用getprice方法
obj.price = 200  # 修改price属性，obj.price = 200 自动调用setprice方法
print(obj.price)
del obj.price    # 删除price属性，自动调用 delprice方法



class Goods(object):
    def __init__(self):
        self.__money = 100

    @property
    def price(self):
        return self.__money

    @price.setter
    def price(self,value):
        self.__money = value
        return self.__money

    @price.deleter
    def price(self):
        del self.__money
        print("Delete Finished!!!")


obj = Goods()   # 创建Goods对象，自动调用__init__方法
print(obj.price) # 打印price属性，自动调用@property下的方法
obj.price = 200  # 修改price属性，自动调用@price.setter方法
print(obj.price)
del obj.price    # 删除price属性，自动调用@price.deleter方法
