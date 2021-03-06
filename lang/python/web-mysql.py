#0.数据库的备份与恢复、创建有权限的用户、搭建主从数据库
"""
用户密码修改:
    首次设置密码:
        mysql -u用户名 password
    修改密码:
        mysql -u用户名 -p旧密码 password 新密码
数据库的备份与恢复:
    备份：
        mysqldump -uroot -p 数据库名 > 指定目录下以sql为后缀的备份文件
        eg:
            -u用户名
            -p密码
            --all-databases所有数据库
            --lock-all_tables备份时禁止修改

            --备份数据库 test
            mysqldump -uroot -p test > testdump.sql
            --备份数据库的python数据表
            mysqldump -uroot -p test.python > testpython.sql
            --备份所有数据库到D:/alldump.sql
            mysqldump -uroot -p --all-databases --lock-all-tables > D:/alldump.sql

    还原:
        mysql -uroot -p 新的数据库名 < 指定目录下以sql为后缀的备份文件


创建数据库的子账号(创建数据库账号并分配权限，可以减小误删数据库的可能性):
    已经创建的账号可以用root(拥有最高权限的账户)账户登录mysql:
    进入mysql数据库中的user表查看,可以查看密码(经过加密)以及用户名;可以直接通过向user表中插入数据来创建用户，删除数据来删除用户
        eg:
            select user,host from user;

    创建新用户:
        grand 权限 on 数据库 to '用户名'@'访问主机' identified by '密码';
        常见的权限:
            update---->更新权限
            select---->查看权限
            all privileges---->所有权限
        eg：
            --给laowang对数据表python（在test数据库中）的查看权限，密码为123
            grant select on test.python to 'laowang'@'localhost' identified '123';
            --使用laowang账户
            mysql -ulaowang -p123

    查看用户权限:
        show grants for 用户名@主机名;
        eg:
            --查看root的权限
            show grants for root@localhost;

    修改用户权限:
        update user set authentication_string=password('新密码') where user='用户名';
        刷新权限(修改密码后必须刷新权限):
            flush privileges;
        eg:
            --修改老王的密码为123
            update user set authentication_string=password('123') where user='laowang';
            flush privileges;


    删除用户:
        drop user '用户名'@'主机名';
        并刷新权限:
            flush privileges;
        eg:
            --删除localhost的laowang
            drop user 'laowang'@'localhost';
            flush privileges;

    远程登陆(为防止数据泄露一般不使用):
        修改mysql的配置文件(ubuntu下为:/etc/mysql/mysql.conf.d/mysqld.cnf文件)，注释掉bind-address,
        重启mysql,远程使用mysql -h IP地址  -u 用户名  -p 远程主机mysql端口


主(master)从(slave)服务器的搭建：
    特别注意：
        主服务器中:server_id生效，log_bin生效
        从服务器中:server_id生效，log_bin不生效
        主服务的server_id与从服务器的server_id必须不同;一般主服务器的server_id=1,从服务器的server_id=2,多个从服务器的server_id可以写同一个值

    主服务器；
        1.导出数据库的数据到.sql文件
        2.修改mysql的配置文件
            server-id=（一个数字）
            log_bin=（此处一般保持不变）
        3.重启mysql服务器
        4.创建用于主从服务器同步的账户
            进入mysql
            grant replication slave  on *.* to '从服务器用户名（slave）'@'主机名' identified by '密码';
            刷新权限；
            flush privileges;
    从服务器:
        1.导入从主服务器导出的.sql文件
        2.修改mysql的配置文件
            server-id=（一个数字）
            注释掉log_bin=
        3.链接到主服务器
            change master  to master_host='主服务器ip', master_user='主服务器为从服务器创建用户的用户名（slave）', master_password='账户密码',
            master_log_file='',master_log_pos= ;
            eg:
                change master to master_host='10.0.2.15',master_user='slave',master_password='1234',
	            master_log_file='mysql-bin.000001',master_log_pos=154;
            注意：
                master_log_file和master_log_pos可以在主服务器查看；
                方法:
                    在主服务器的mysql中输入：
                        show master status;
                将show master status显示的,file填入master_log_file,postion填入master_log_pos
        4.检查从服务器是否与主服务器链接成功
            在从服务器的mysql中输入:
                show slave status \G;
                显示的结果中:
                    Slave_IO_Running: Yes
                    Slave_SQL_Running: Yes
                表示链接成功

"""



#1.数据库的使用，数据表的使用
"""
sql数据库中的表:
    行---->标记                  列---->字段(*代表所有字段)

sql数据表常用的数据类型:
    整数类型：BIT、BOOL、TINY INT、SMALL INT、MEDIUM INT、 INT、 BIG INT
    浮点数类型：FLOAT、DOUBLE、DECIMAL
    字符串类型：CHAR、VARCHAR、TINY TEXT、TEXT、MEDIUM TEXT、LONGTEXT、TINY BLOB、BLOB、MEDIUM BLOB、LONG BLOB
    日期类型：Date、DateTime、TimeStamp、Time、Year
    其他数据类型：BINARY、VARBINARY、ENUM、SET、Geometry、Point、MultiPoint、LineString、MultiLineString、Polygon、GeometryCollection等

    枚举类型(数据只能是括号中的其中一个):
        enum(枚举1，枚举2，枚举3.。。。。枚举N)
        eg:
            enum("男","女")

sql语句(以Linux版为基础):
1)
    链接数据库:
        mysql -u用户名(一般最高权限的为root) -p密码
    退出客户端:
        quit
        exit
        ctrl+d
    重启mysql:
        service mysql restart

2)数据库
    sql语句要有分号;结尾
    显示时间:
        select now();
    显示版本
        select version();
    查看数据库:
        show databases;
    创建数据库 编码一般写utf8
        create database 数据库名；
        create database 数据库名  charset=编码;
    查看创建的数据库:
        show create database 数据库名;
    删除数据库:
        drop database 数据库名;

3)数据表
    显示当前使用的数据库:
        select database();
    切换/使用数据库:
        use 数据库名;
    查看数据库中的数据表（select database();结果不为NULL）:
        show tables;
    查看数据表的结构:
        desc 数据表名;
    创建数据表:
        create table 数据表名(字段 类型 约束[,字段 类型 约束]);
        eg：
            # 将age设置为主键,name不允许为空(约束可以有多个)
            create table people(
                age int primary key,
                name varchar[30] not null
            );
    数据表插入标记(列):
        insert into 数据表名 values(字段1的值，字段2的值，字段3的值...);
    查看数据表的内容(标记、字段):
        select * from 数据表名;
    删除数据表:
        drop table 数据表名;
    eg：
        --auto_increment：自动增加
        --primary key:主键
        --not null：不允许为空
        --enum("男"，"女")：男或女
        --unsigned：无符号类型(只有正数)
        --default：默认值
        --decimal(5,2):共5位，小数点后有2位
        create table student(
            id int unsigned not null auto_increment primary key,
            name varchar(30),
            age tinyint unsigned default 0,
            high decimal(5,2),
            sex enum("男","女","保密") default "保密"
        );
        insert into student value(0,"老王",18,170.9,"男");
        select * from student;
4)数据表结构
    增加字段：
        alter table 数据表名 add 字段名 类型 约束;
    修改字段约束:
        alter table 数据表名 modify 字段名 类型 约束;
    修改字段名及约束:
        alter table 数据表名 change 原名  新名 类型 约束;
    删除字段:
        alter table 数据表名 drop 字段名;
5)数据的增删改查(标记)
    插入数据:
        注意；有auto_increment的地方可以填写0或null或default
        需要填写所有字段(列)的值(插入多个数据):
            insert into 数据表名 values(字段1的值，字段2的值，字段3的值...),
                (字段1的值，字段2的值，字段3的值...)...;
        部分插入（只需要填写部分字段）(插入多个数据):
            insert into 数据表名 (字段1,字段2...)  value (值1,值2...),
                (值1,值2...)...;
    修改数据:
        update 数据表名 set 字段1=值1,字段2=值2...  where 条件;
    数据删除(删除标记列)(物理删除):
        delete from 数据表名 where 条件;
        delete from 数据表名;--删除数据表中的所有内容
    数据查询:
         全部查询:
            select * from 数据表名;
        部分查询:
            select 字段1，字段2... from 数据表名 where 条件;
        部分查询并用as为字段创建别名:
            select 字段1 as 别名1,字段2 as 别名2... from 数据表名 where 条件;
        部分查询并用as为数据表创建别名:
            select 数据表别名.字段1,数据表别名.字段2.....  from 数据表名  as 数据表别名;
        重复筛选(清除重复行):
            select distinct 字段1,字段2... from 数据表名;

sql中的删除一般不真正的删除数据，而是用一列(字段来标记是否删除)


"""



#2.数据表的查询
"""
sql的查询:
    1)普通查询
        全部查询:
            select * from 数据表名;
        部分查询:
            select 字段1，字段2... from 数据表名;
        部分查询并用as为字段创建别名:
            select 字段1 as 别名1,字段2 as 别名2... from 数据表名;
        部分查询并用as为数据表创建别名:
            select 数据表别名.字段1,数据表别名.字段2.....  from 数据表名  as 数据表别名;
        重复筛选(清除重复行):
            select distinct 字段1,字段2... from 数据表名;
    
    2)条件查询(where 条件)
        条件格式支持:
            比较运算符: 大于 > ,小于 < ,是否相等 = ，大于等于 >= ,小于等于 <= ,不等 !=
            逻辑运算符: 与 and ,或 or ,非 not
            可使用一对小括号()改变优先级顺序，保证条件的正确执行
                eg:  select id,age from student where not not (age!=11  and age!=22);
    
    3)模糊查询
        like：%---->替换一个或多个
                _---->替换一个
            select 字段1,字段2....  from where 某字段 like like表达式;
            eg:
                select id,name from student where name like "小_";--查询以小开头，并且名字有两个字
                select id,name from student where name like "张%";--查询名字中性张的人
                select id,name from student where name like "%三%"--查询名字中有三的人
                
        rlike: 正则表达式
            select 字段1,字段2....  from where 某字段 rlike 正则表达式;
            eg:
                select id,name from student where name rlike "^李.*$";  --查询性李的人
                select id,name from student where name rlike "^.*三.*&" --查询姓名中有三的人
    
    4)范围查询
        查询不连续多个in或not in:
            在(in (...)):  select 字段1,字段2... from 数据表名 where 某字段 in (值1,值2...);
            不在(not in (...)):   select 字段1,字段2... from 数据表名 where 某字段 not in (值1,值2...);
        查询在某范围内:
            在之间(between...and...):     select 字段1,字段2... from 数据表名 where 某字段 between 值1 and 值2;
            不在之间(not between...and..):     select 字段1,字段2... from 数据表名 where 某字段 not between 值1 and 值2;
        空判断:
            为空(is null):    select 字段1,字段2... from 数据表名 where 某字段 is null;
            不为空(is not null):    select 字段1,字段2... from 数据表名 where 某字段 is not null;
    
    
sql排序:
    排序方法:
        从小到大: asc
        从大到小: desc
    1)从小到大(默认):order by 排序字段 asc;
        A)最简版:按照主字段从小到大
        select 显示字段1，显示字段2... from 数据表 where 条件;
        B)进化版:按指定字段从小到大
        select 显示字段1，显示字段2... where 条件 from 数据表 order by 排序字段;
        C)究极版:并无太大卵用
        select 显示字段1，显示字段2... from 数据表 where 条件 order by 排序字段 asc;
        
    2)从大到小: order by 排序字段 desc;
        select 显示字段1，显示子段2... from 数据表 where 条件 order by 排序字段 desc;
        
    3)多个字段排序: order by 排序字段1 排序方法1,排序字段2 排序方法2,...;
        select 显示子段1，显示字段2... from 数据表 where 条件 order by 排序字段1 排序方法1,排序字段2 排序方法2,...;
        
        
        

sql聚合函数:
    用法: 函数(字段或函数)
    1)总数:count(字段)
        select counte(计数字段) from 数据表 where 条件;
    
    2)最大值:max(字段)   最小值: min(字段)
        select max(字段) from 数据表 where 条件;
        select min(字段) from 数据表 where 条件;
        
    3)平均值:avg(字段)
        select avg(字段) from 数据表 where 条件;
        
    4)4舍5入: round(字段)
        select avg(字段) from 数据表 where 条件;
        
        
sql分组(配合聚合函数使用否则无大的卵用):
    用法: group by 分组字段
    1)显示分组后,组内的内容: group_concat(字段1,字段分隔1(可有可无),字段2,字段分隔2...)---->group_concat()显示的字段会自动连接在一起
        select 分组字段,group_concat(...) from 数据表名 where 条件 group by 分组字段;
        
    2)分组后筛选: having 条件
        having:分组后，对每个组进行筛选
        where:分组前，对数据表数据筛选
        select 分组字段 from 数据表 group by 分组字段 having 条件;
        
        
sql分页:
    limit start,count
    limit (第N页-1)*每页的个数，每页的个数
    语法:
        select 显示字段 from 表 where 条件 limit 个数;
        select 显示字段 from 表 where 条件 limit 开始,个数;
   
   
sql关联查看:
    on：
        要关联的字段
    关联方式:  inner:表1表2取交集
               left:以左边的表为基准
               right:以右边的表为基准
    语法:
        select 表.字段 from 表A inner join 表B on 表A.字段=表B.字段;
        select 表.字段 from 表A left join 表B on 表A.字段=表B.字段;
        select 表.字段 from 表A right join 表B on 表A.字段=表B.字段;
        

自关联表:
    eg:china(id,name,parent_id);
    id          name            parent_id
    1           北京              0
    2           湖北              0
    ...
    101         海淀区             1
    102         朝阳区             1
    ...
    201         武汉               2
    202         黄石               2
    ...
    
    id---->每个地区的唯一标记
    name---->地区名
    parent_id---->隶属于那个地区
    
    可以通过parent_id来筛选从而获取想要的数据
    例如:
        想找到湖北武汉
        A.select * from china where parent_id=0;找到所有的省份id,找出湖北的id为2----->B.select * from china where parent_id=2;找到武汉的id
        

子查询:
    select语句里有sekect语句
    eg:
        select * from student where hight=(select max(hight) from student);
        
"""


#3.数据库编写的一些规范
"""
三范式(Normal Form)：拆表
    第一范式(1NF)：
        不能再拆
        eg:张三、11、152...7777     --拆分-->     张三       11        152...7777
        
    第二范式(2NF)：
        其余字段必须直接依赖于主键
        eg：                                                                                                                          订单号   购买数量  地址
                订单号  产品单号  产品名称  单价  折扣  购买数量  地址 ----通过订单号不能查出唯一商品，通过产品单号不能查出购买信息,拆分------>    产品单号  产品名称  单价  折扣
    
    第三范式(3NF)：
        不合适就拆表
        
一对一:建一个或多个表
多个一关系时:将标记字段写在 多的 表中
多对多关系时:新建一个表

"""


#4.事务、索引
"""
事务(python中默认开启事务):
    特点：
        原子性(atomicity)---->多个mysql修改要么一次成功，要么不成功不修改(开启事务后，写多个修改mysql的语句,提交则一次执行所有修改,不提交则不修改mysql的任何数据)
        一致性(consistency)---->未commit(提交)前数据不修改，在另一个mysql_client中查看表数据也不会改变
        隔离性(isolation)---->一个mysql_client在修改时禁止另一个mysql_client修改
        持久性(durability)---->持久保存数据
    开启事务:
        start transaction;/begin;
    提交:
        commit;
    eg:
        mysql中执行:                                start transaction;
            update .........;     -----可视为-----> update  ......;
                                                    commit;
                                                    
索引(创建索引能够提高查找的效率):
    创建索引的方法:
        数据为int类型时无需写长度
        数据为varchar类型时长度建议与字段varchar的长度一致
        create index 索引名称 on 表名(字段名称(长度));---->两个小括号均不能丢
        eg： 
            create index num_in on python_table(name(20));
    删除索引:
        drop index 索引名称 on 表名;
        eg：
            drop index num_in on python_table;
    
            
"""



"""
总结:
    使用.sql文件导入sql语句:
        source 文件名.sql;
    1.数据库操作
        链接数据库:
            mysql -uroot -p密码
        退出客户端:
            quit
            exit
            ctrl+d
        
        1)数据库
            sql语句要有分号;结尾
            显示时间:
                select now();
            显示版本
                select version();
            查看数据库:
                show databases;
            创建数据库 编码一般写utf8
                create database 数据库名；
                create database 数据库名  charset=编码;
            查看创建的数据库:
                show create database 数据库名;
            删除数据库:
                drop database 数据库名;
        
        2)数据表
            显示当前使用的数据库:
                select database();
            切换/使用数据库:
                use 数据库名;
            查看数据库中的数据表（select database();结果不为NULL）:
                show tables;
            查看数据表的结构:
                desc 数据表名;
                        
    2.数据表操作(数据表支持inner/left/right的数据表之间的操作)
        增加字段：
            alter table 数据表名 add 字段名 类型 约束;
        
        修改字段约束:
            alter table 数据表名 modify 字段名 类型 约束;
        
        修改字段名及约束:
            alter table 数据表名 change 原名  新名 类型 约束;
        删除字段:
            alter table 数据表名 drop 字段名;
        
        添加外键(约束，只能是指定外键中有的标记)(两个表:数据表、外键表):
            alter table 数据表名 add foreign key (数据表中的要关联的外键，要加小括号) references  外键表名(外键表中要关联的外键，此处括号不能省略); 

        删除(解绑)外键(先用desc查看表中有哪些外键):
            alter table 数据表名 drop foreign key  外键名称;
            
        创建视图(创建虚拟的表,从老表中筛选数据来组成一张假表，并不是真的创建):
            create view 视图名 as select语句;
            
        删除视图:
            drop view 视图名;
            
    3.数据操作
        1)数据插入(支持插入另外一个表)
            需要填写所有字段(列)的值(插入多个数据):
                insert into 数据表名 values(字段1的值，字段2的值，字段3的值...),
                    (字段1的值，字段2的值，字段3的值...)...;
            部分插入（只需要填写部分字段）(插入多个数据):
                insert into 数据表名 (字段1,字段2...)  value (值1,值2...),
                    (值1,值2...)...;
            插入另外一表中的某些字段:
                insert into 数据表名（数据表中的某字段） (另外数据表的字段，一般由select筛选出来，直接写select不用写小括号)           
       
        2)修改数据(可以使用另外一表的某些字段来更新修改):
            普通修改:
                update 数据表名 set 字段1=值1,字段2=值2...  where 条件;  
            用另外一个数据表来修改(更新数据表):
                 update 数据表名 inner join 更新数据表 on 两数据表中相应字段的更新条件 set 数据表的.某字段=更新数据表.某字段(一般是主键字段);
        
        3)数据删除
            delete from 数据表名 where 条件;
        
        4)数据查看
            细节写法:
            1.select 显示字段N 
            显示字段N(更换写法顺序可以改变显示顺序):
                1)字段1,字段2...
                2)表名1.字段1,表1.字段2,...表2.字段1,表2.字段2...
                3)函数(字段)---->显示函数结果
            2.from 表N
            表N(可以写一个表，也可以写关联表):
                关联方式:inner/left/right
                1)单表：数据表名
                2)多表: 数据表A 关联方式 join 数据表B on 表A.字段=表B.字段
            3.where 表筛选的条件
            对表的字段进行筛选
                筛选条件支持算术筛选(>/</=/!=)、逻辑筛选(and/or/not)、判断筛选(is null/is not null)、范围筛选(between...and.../not between...and...)
            4.having 分组后的条件筛选
            对分组或分页后的内容进行筛选
            5.group by 分组条件
            分组
            6.limit start,count
            分页
            7.order by 排序字段 排序方式
            排序方式:asc(从小到大(默认))、desc(从大到小)
                1)单依据：order by 排序字段 排序方式;
                2)多依据：order by 排序字段1 排序方式1,排序字段2 排序方式2...;
        
            select 显示字段N from 表N where 表格筛选条件 group by 分组条件 having 分组后筛选的条件  order by 排序依据N limit (第N页-1)*每页的个数,每页的个数;
            eg:
                --显示20<id<100
                select * from table2 where id>20 and id<100;
                
                --按name分组，显示每组name中有"李"的
                select * from table2 group by name having name=`%李%`;
                
                --筛选id>33的并按照class从大到小
                select * from table2 where id>33 order by class desc;
                
                --筛选id>20的，显示第5页的6个
                select * from table2 where id>20 limit (5-1)*6,6;
            
                --选table1与table2内关联,并重命名为t1、t2，table2的class_id与table1的id关联,显示table1的class与table2的name
                （table1结构:id,class        table2结构:id,name,class_id）
                select t1.class,t2.name from table1 as t1 inner join table2 as t2 on t2.class_id=t1.id;

"""









































