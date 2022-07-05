"""
python操作mysql的一般流程:
查看:
    1.创建connection---->2.获取cursor（游标）---->3.执行sql语句---->4.关闭cursor---->5.关闭connection
增、删、改:
    1.创建connection---->2.获取cursor（游标）---->3.执行sql语句---->4.connection对象提交(提交才会生效，也可撤回)---->5.关闭cursor---->6.关闭connection
"""


import pymysql
from pymysql import *
import sys

"""1简单查看"""

#
# def main():
#     #创建链接
#     con = connect(host="localhost",port=3306,user="root",password="123456",database="world")
#     #获取cursor对象
#     cur = con.cursor()
#     #执行sql语句
#
#     counte = cur.execute("select * from city;") #返回数据的标记数
#     cur_result1 = cur.fetchone()  # 查看一个标记，返回一个元组
#     cur_result2 = cur.fetchmany(5)  # 查看5个标记，返回一个二维元组
#     cur_result3 = cur.fetchall()   # 查看所有标记，返回一个元组
#
#     print(cur_result1)
#     print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#     print(cur_result2)
#     print("..........................................")
#     print(cur_result3)
#
#     #关闭cursor
#     cur.close()
#     #关闭connection
#     con.close()
#
# if __name__=="__main__":
#     main()


"""2增、删、改、查"""
class Sql_Func():
    def __init__(self):
        # 创建连接
        self.con = connect(host="localhost", port=3306, user="root", password="123456", database="test")
        # 创建游标
        self.cursor = self.con.cursor()

    #插入标记
    def insert(self):
        name=input("name:")
        age=input("age:")
        height=input("height:")
        sex=input("sex('man','woman','unkown'):")
        sql = """insert into student values(0,"{0}",{1},{2},{3},1);""".format(name,age,height,sex)
        self.cursor.execute(sql)
        # 提交
        self.con.commit()
        # 撤回
        # self.con.rollback()

    #删除标记
    def delete(self):
        sql = """delete from student where id=%s;""" % input("id:")
        self.cursor.execute(sql)
        # 提交
        self.con.commit()
        # 撤回
        # self.con.rollback()

    #修改
    def change(self):
        id=input("id:")
        name = input("name:")
        age = input("age:")
        height = input("height:")
        sex = input("sex('man','woman','unkown'):")
        sql = """update student set name="{1}",sex={2},age={3},height={4}  where id={0} ;""" .format(id,name,sex,age,height)
        self.cursor.execute(sql)
        #提交
        self.con.commit()
        #撤回
        # self.con.rollback()

    #查看
    def see(self):
        sql = """select * from student;"""
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for i in result:
            print(i)

    #退出
    def exit(self):
        #关闭游标
        self.cursor.close()
        #关闭连接
        self.con.close()

# 主菜单
def main_meun():
    print("------>1.插入")
    print("------>2.删除")
    print("------>3.更新修改")
    print("------>4.查看")
    print("------>5.退出")
    return input("请选择:")


def main():
    while True:
        #函数执行
        option = main_meun()
        if option=="1":
            Sql_Func().insert()
        elif option=="2":
            Sql_Func().delete()
        elif option=="3":
            Sql_Func().change()
        elif option=="4":
            Sql_Func().see()
        elif option=="5":
            Sql_Func().exit()
            break
        else:
            pass
    print("OVER!!!")


if __name__=="__main__":
    main()