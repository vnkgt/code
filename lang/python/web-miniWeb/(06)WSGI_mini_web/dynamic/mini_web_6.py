"""
添加mysql功能
"""
import pymysql
import re
#本地文件文件读取函数字典
GLOBAL_URL_DIC = dict()
#路由修饰器
def route(func_name):
    def dic_add_dec(func_name_pointer):
        GLOBAL_URL_DIC[func_name] = func_name_pointer
        def dec_func(*args,**kwargs):
            return func_name_pointer(*args,**kwargs)
        return dec_func
    return dic_add_dec

@route("index.html")
def index():
    return "<h1>This is Index!!!</h1>"

@route("center.html")
def center():
    return "<h1>This is center!!!</h1>"


@route("login.html")
def login():
    return "<h1>This is Login!!!</h1>"

#请求的数据是mysql的数据
@route("mysql.sql")
def mysql():
    # 创建链接
    mysql_connect = pymysql.connect(host="localhost", port=3306, user="root", password="123", database="china")
    # 创建游标
    mysql_cursor = mysql_connect.cursor()
    # sql语句查询数据库
    mysql_cursor.execute("select * from china;")
    mysql_get_data = mysql_cursor.fetchall()
    # 数据模板
    data_template = """<h1>
        <td>id:{0}      </td>
        <td>name:{1}        </td>
        <td>parent_id:{2}</td>
    </h1>\r\n
    """
    mysql_back_body = str()
    for i in mysql_get_data:
        mysql_back_body += data_template.format(i[0], i[1], i[2])
    # 关闭游标
    mysql_cursor.close()
    # 关闭链接
    mysql_connect.close()
    return mysql_back_body

def application(env,set_head_func):
    print("------------->",env["PATH_INFO"],"<-------------------")
    try:
        set_head_func("200 OK", [("Content-Type:", "text/html;charset=utf-8")])
        return GLOBAL_URL_DIC[env["PATH_INFO"]]()
    except:
        set_head_func("404 NOT FOUND", [("Content-Type:", "text/html;charset=utf-8")])
        return "<h1>NOT EXIST IN LOCAL!!!</h1>"


#测试mini_web.py是否导入成功
def test():
    print("Successful import mini_web__4!!!")