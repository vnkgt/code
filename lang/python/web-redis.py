"""
redis与python的交互:
    安装redis模块
    创建StrictRedis对象链接redis数据库===>reidis操作

"""
from redis import *

def main():
    try:
        #host:redis的IP地址,port:redis的port号,db:数据库编号(一般0-15,一般选零)
        sr = StrictRedis(host="localhost",port=6379,db=0)
        #添加一个key
        sr.set(name="aa",value="123456")
        #获取"aa"的值
        print('the value of "aa":\t\t',sr.get("aa"))
    except Exception:
        print("error")


if __name__ == "__main__":
    main()
