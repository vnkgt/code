#python命令执行.py文件时给.py文件传参
"""
除了通过读取配置问价来配置http服务器外，还可以通过给程序传参数来配置http服务器（一般linux常用传参的方法来配置）：
    该功能的实现需要使用sys模块下的argv方法：
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
    (eg:D:/Code/python/venv/Scripts)
2.cd 进入所要运行的.py文件的目录下
    （cd: D:/Code/python/2_reviwe/2.Web operation/1.web/(04)WSGI_mini_web）
3.在pycharm下端的Terminal输入命令即可运行
    (eg: python 1.py---->即可运行1.py)
    (eg:python 1.py aaa bbb ccc---->即可给1.py传递参数aaa、bbb、ccc(参数通过sys.argv来查看))
"""
print(sys.argv)