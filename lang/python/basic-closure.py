#闭包
"""
闭包:
    函数内套有函数
    在闭包的子函数内修改上级的变量需要使用nonlocal
    eg:
        def main_func(arg1,arg2...):
            def son_func1(son1_arg1,son2_arg2):
                pass
            def son_func2():
                pass
"""

def line(k,b):
    def func(x):
        return k*x+b
    return func

line_t = line(3,2)
for i in range(4):
    print(line_t(i))

