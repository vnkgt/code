#给.py问价传参(一般在liunx中使用)
"""
    给.py程序传参的方法：
        1.保证能在命令行模式(Terminal)下能运行python程序(python A.py----->运行A.py)
        1.1能在命令行模式下使用命令来运行程序要保证两点:
            1)存在命令的环境变量(eg：python.exe在D:\python下------->就在环境变量中添加D:/python)
            2)进入了要运行文件的文件夹(eg:要运行1.py而1.py在D:/CODE下------>cd进入D:/CODE)
            补充:在Terminal下输入：python 1.py aa bb cc------>即可运行1.py,并在sys.argv中有["1.py","aa","bb","cc"]
        2.在python程序中:
            sys.argv-------->返回输入命令的列表（命令以空格分隔来组成列表，列表中的元素均为字符串）
                                                通过列表对列表中的字符串（正则表达式）分析，来提取想要的参数


    eg：
        在linux下输入
        python3 http_server 7788 mini_web:application
        sys.argv--------->返回["python3","http_server","7788","mini_web:application"]
"""

import sys
#在window下使用命令来运行.py文件
"""
1.在pycharm->run->Edit Configurations->parameters中添加python.exe所在的问价夹
    (eg:D:\Code\python\venv\Scripts)
2.cd 进入所要运行的.py文件的目录下
    （cd: D:\Code\python\2_reviwe\2.Web operation\1.web\(04)WSGI_mini_web）
3.在pycharm下端的Terminal输入命令即可运行
    (eg: python 1.py---->即可运行1.py)
    (eg:python 1.py aaa bbb ccc---->即可给1.py传递参数aaa、bbb、ccc(参数通过sys.argv来查看))
"""
print(sys.argv)