#import模块导入问题
"""
import导入模块:
    1.import导入模块路径的先后顺序，可以通过sys模块中的sys.path方法查看；
    2.sys.path返回一个列表，列表中的先后顺序代表import查找模块的先后顺序；
        可以通过修改sys.path列表中的值来修改import导入模块的先后顺序.
    3.ret = __import__(模块名)---->返回一个指向模块的对象(但首先该模块在sys.path中存在)
      func = getattr(模块对象,"函数名")------>返回一个对象:该对象指向模块下的的某个函数
          eg:
            module_name = "AAA"
            ret = __import__(module_name)---->ret指向AAA模块
            func = getattr(ret,"test")------->func指向AAA模块下的test方法
            func("aa","bb")------------------>相当于AAA.test("aa","bb")


import重新导入模块:
    方法:
        from imp import reload
        reload(module)

"""
ret = __import__("os")
path = getattr(ret,"path")
print(path)