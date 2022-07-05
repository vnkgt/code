import pymysql
#创建链接
mysql_connect = pymysql.connect(host="localhost", port=3306, user="root", password="123", database="china")
# 创建游标
mysql_cursor = mysql_connect.cursor()
#sql语句查询数据库
a = mysql_cursor.execute("select * from china;")
print(a)
# mysql_get_data = mysql_cursor.fetchall()
#
# #数据模板
# data_template = """<th>
#     <td>id:{0}</td>
#     <td>name:{1}</td>
#     <td>parent_id:{2}</td>
# </th>
# """
# mysql_back_body = str()
# for i in mysql_get_data:
#     mysql_back_body += data_template.format(i[0],i[1],i[2])
#
# print(mysql_back_body)
# #关闭游标
# mysql_cursor.close()
# #关闭链接
# mysql_connect.close()