import random
name = ["laowang","老李","张三","李四","王五","朝气","桑三炮","喜羊羊","dio","jojo","max","kk","老李","张三","李四"]
age = list(random.randint(18,55) for i in range(len(name)))
sex_list = ["man","woman","unknow"]
sex = list(random.randint(1,3) for i in range(len(name)))
height = list(random.randint(155,195) for i in range(len(name)))
is_del = list(random.randint(0,1) for i in range(len(name)))
# 创建数据表
line1 ='create table student(' \
       'id int auto_increment primary key not null,\n' \
       'name varchar(20) not null,\n' \
       'age int not null,\n' \
       'height int not null,\n' \
       'sex enum("man","woman","unknow") default "unknow",\n'\
       'is_del bit default 0' \
       ');'

# 数据插入
line2 = str()

for i in range(len(name)):
    line2 += 'insert into student value({0},"{1}",{2},{3},{4},{5});\n'.format("0",name[i],str(age[i]),str(height[i]),str(sex[i]),str(is_del[i]))

with open("C:/Users/Administrator/Desktop/sqlfile.txt","w") as sqlfile:
    data = "床建表\n"+line1+"\n"+"\n\n插入元素\n\n"+line2
    sqlfile.write(data)
    print("OVER!!!")



