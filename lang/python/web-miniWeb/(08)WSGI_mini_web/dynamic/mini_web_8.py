"""
    添加日志功能
"""
import pymysql
import re
import logging
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



@route("login.html")
def login():
    return "<h1>This is Login!!!</h1>"



@route("center.html")
#个人中心
def center():
    # 创建链接
    mysql_connect = pymysql.connect(host="localhost", port=3306, user="root", password="123", database="china")
    # 创建游标
    mysql_cursor = mysql_connect.cursor()
    #sql语句查询个人数据表
    mysql_cursor.execute("select * from my_home;")
    mysql_get_data = mysql_cursor.fetchall()
    #模板
    data_template =  """<h2>id:{0}      home_name:{1}       home_id:{2}</h2>"""
    mysql_back_data = str()
    mysql_back_data += "<h2>This is personal center!!!</h2>"
    for i in mysql_get_data:
        mysql_back_data += data_template.format(i[0],i[1],i[2])
    return mysql_back_data

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
    data_template = """<h2>
        <td>id:{0}      </td>
        <td>name:{1}        </td>
        <td>parent_id:{2}</td>
    </h2>\r\n
    """
    mysql_back_body = str()
    mysql_back_body += "<h1>This is databases of all mysql_databases!!!</h1>"
    for i in mysql_get_data:
        mysql_back_body += data_template.format(i[0], i[1], i[2])
    # 关闭游标
    mysql_cursor.close()
    # 关闭链接
    mysql_connect.close()
    return mysql_back_body

#my_home添加
def client_add(add_id):
    sql_con = pymysql.connect(host="localhost", port=3306, user="root", password="123", database="china")
    sql_cur = sql_con.cursor()
    is_in_china = sql_cur.execute("select * from china where id={0};".format(add_id))
    if is_in_china==0:
        return "<h1>该id不在china中!!!</h1>"+center()
    is_in_my_home = sql_cur.execute("select * from my_home where home_id={0};".format(add_id))
    if is_in_my_home!=0:
        return "<h1>该id已在my_home中!!!</h1>"+center()
    sql_cur.execute("insert into my_home(my_home.home_name,my_home.home_id) select china.name,china.id from china where id={0};".format(add_id))
    sql_con.commit()
    center_data = center()
    return "<h1>已经添加到数my_home据表中!!!</h1>"+center_data

#my_home删除
def client_del(del_id):
    print(del_id)
    sql_con = pymysql.connect(host="localhost", port=3306, user="root", password="123", database="china")
    sql_cur = sql_con.cursor()
    is_in_myhome = sql_cur.execute("select * from my_home where id={0}".format(del_id))
    if is_in_myhome==0:
        return "<h1>不存在该id的标签!!!</h1>"+center()
    sql_cur.execute("delete from my_home where id={0}".format(del_id))
    sql_con.commit()
    center_data = center()
    return "<h1>删除完成!!!</h1>"+center_data


#my_home修改
def client_change(change_id):
    sd_id = change_id.split("_")
    change_id_s = sd_id[0]
    change_id_d = sd_id[1]
    print(change_id_s,change_id_d)
    sql_con = pymysql.connect(host="localhost", port=3306, user="root", password="123", database="china")
    sql_cur = sql_con.cursor()
    is_in_china = sql_cur.execute("select * from china where id={0};".format(change_id_d))
    if is_in_china == 0:
        sql_cur.close()
        sql_con.close()
        return "<h1>目标id不在china中,不能修改!!!</h1>"+center()
    is_in_my_home = sql_cur.execute("select * from my_home where home_id={0};".format(change_id_s))
    if is_in_my_home == 0:
        sql_cur.close()
        sql_con.close()
        return "<h1>源id不在my_home中,不能进行修改!!!</h1>"+center()
    sql_cur.execute("select name from china where id={0};".format(change_id_d))
    home_name_inchina = sql_cur.fetchone()[0]
    sql_cur.execute("update my_home set home_id={0},home_name='{1}' where home_id={2};".format(change_id_d,home_name_inchina,change_id_s))
    sql_con.commit()
    sql_cur.close()
    sql_con.close()
    center_data = center()
    return "<h1>已经修改my_home中的数据!!!</h1>"+center_data


@route("change_func")
def change_func(request):
    request_data = request.split("/")
    print(request_data)
    change_mode = request_data[1]
    change_id = request_data[2]
    print("change_mode-->{0}<--change_id-->{1}<--".format(change_mode,change_id))
    if change_mode=="add":
        return client_add(change_id)
    elif change_mode=="change":
        return client_change(change_id)
    elif change_mode=="delete":
        return client_del(change_id)
    else:
        return "<th>不存在该修改指令!!!</h1>"+center()


def application(env,set_head_func):
    #创建logger对象
    logger = logging.getLogger()
    logger.setLevel(logging.WARNING)
    log_file = logging.FileHandler("logging.txt",mode="a")
    log_file.setLevel(logging.WARNING)
    log_show = logging.StreamHandler()
    log_show.setLevel(logging.WARNING)
    format = logging.Formatter("%(asctime)s--->%(filename)s{line:%(lineno)d}--->%(levelname)s")
    log_file.setFormatter(format)
    log_show.setFormatter(format)
    logger.addHandler(log_file)
    logger.addHandler(log_show)
    try:
        #固定页面请求
        set_head_func("200 OK", [("Content-Type:", "text/html;charset=utf-8")])
        if env["PATH_INFO"] in GLOBAL_URL_DIC:
            return GLOBAL_URL_DIC[env["PATH_INFO"]]()
        #动态修改请求(格式change/修改模式/修改的数据)
        else:
            return change_func(env["PATH_INFO"])
    except:
        logging.warning("没有找到%s"%env["PATH_INFO"])
        set_head_func("404 NOT FOUND", [("Content-Type:", "text/html;charset=utf-8")])
        return "<h1>NOT EXIST IN LOCAL!!!</h1>"


#测试mini_web.py是否导入成功
def test():
    print("Successful import mini_web__4!!!")