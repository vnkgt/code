#orm
"""
django的核心思想:orm（object relational mapping）对象关系映射

orm思想:
    用对象来对应数(mysql)据表,通过对对象操作来修改数据表
orm实现方法:
    元类+继承
"""
import re
#定义一个处理对象的元类对象，用于处理子对象的属性，将其装换为便于转换为sql语句的形式
class orm(type):    #继承type实现元类
    def __new__(cls,sonclass_name,sonclass_father_tuple,sonclass_attrs_dic):
        #使用传入的子类信息创建数据表
        new_field = dict()           #用来储存创建字段的信息(key用来对应对象的名称，value对应该字段的value值)
        sql_values = str()            #创建数据表时的value
        #提取属性字典中的，创建字段的元组(key取键，value取值)
        for key,value in sonclass_attrs_dic.items():
            #判断是否为创建字段的元组
            if isinstance(value,tuple) and len(value)==2:
                new_field[value[0]] = value[1]
                sql_values += value[0]+" "+value[1]+","
            new_field[key] = value
        sql_values = re.match(r"^(.*),$",sql_values).group(1)

        #使用提取的信息写sql语句创建sql数据表
        create_new_sql_table = """create table {0}({1});""".format(sonclass_name,sql_values)  #使用子对象的名字作为表名
        new_field["create_table"] = create_new_sql_table
        #回传重新关联的类属性(new_field{类对象名:对应字段创建的字段信息})
        return type.__new__(cls,sonclass_name,sonclass_father_tuple,new_field)

#该对象对应一个表
class Table_A(object,metaclass=orm): #继承元类
    #表中的字段(字段名称,限制条件)
    url_id = ("id","int primary key")
    url_name = ("name","varchar(20)")
    url_age = ("age","int")

    def __init__(self):
        pass

    def save(self):
        #打印经元类修改过后，添加的create_table属性
        print("This is save in Table_A:\n",self.create_table)

t = Table_A()
t.save()
print("Table_A的所有属性:",dir(t))
