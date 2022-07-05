"""
    0)列表、元组、字典(list:列表对象    tuple:元组对象   dict:字典对象)
        len(list)   len(tuple)   len(dict)   获取列表、元组、字典的长度
        列表:
            创建:     list = []   list = list()
            将可迭代对象转换为列表:        list(Iterable)
            list.append(obj)                   列表末尾添加obj
            list.insert(place,obj)             列表的place处插入obj，place可以为小于等于-1的负整数代表从列表后向前数
            list.remove(obj)                   列表删除第一个obj
            list.index(obj,unm)                列表中查找obj的下标，若有多个相同元素默认返回第一个查找到的元素的下标
            list.clear()                       删除列表中的所有元素
            list.copy()                        复制list
            list.extend(string)                 为列表中的每个字符串元素后加上string
            list.count(obj)                     计算列表中obj出现的次数
            list.reverse()                      将列表中的元素翻转
            list.sort()                         将列表从小到大整理排序，若有参数reverse=True则表示倒序排
            list.split(start:end:step)           列表的start到end每隔step取一个元素(start:end均可正可负)
            list[index_num].join(string)         列表下标为index_num的字符串后添加string

        元组:(不可变，不可修改Iterable)
            tuple(Iterable)             将一个可迭代对象转换为元组
            eg:   t1 = tuple([1,2,3,4])
                    t2 = tuple({"a":1,"f":3})

        字典:(键值对key:value)     key的名字可以任意取，value的值也可是任意值
            创建:     dict = dict(key1= value1, key2= value2.......keyN= valueN)                          key不需要加引号
                      dict = dict(zip(["key1", "key2" ......"keyN"],[value1, value2.....valueN]))         key需要加引号
                      dict = dict([("key1",value1),("key2",value2),......("keyN",valueN)])                key需要加引号

            dict.updata(dict1)                                     向字典当中添加dict1
            dict["keyName"] = value                                若keyName存在则修改，不存在则添加
            del dict["keyName"]                                     删除指定keyName的键值对
            keyName in dict                                         判断keyName是否在字典当中
            dict["keyName"]                                         返回keyName对应的值


    1)系统命令sys模块
        sys.exit()              退出
        补充:
            运行cmd命令:os模块
                os.system(cmdcommond)    在cmd中运行cmdcommond语句

    2)异常处理
    try:
        语句块
    except Exception as error:
        语句块异常时，执行的出路语句
    else:
        语句块(try未出现错误时执行)
    finally:
        无论语句块是否正常执行，最后都要执行的语句

"""

"""0)列表、元组、字典"""
#   A.列表
# def main():
#     # 创建列表
#     list1 = []
#     list2 = list()
#
#     # 添加元素  apppend(obj)
#     list1.append(1)
#     list1.append(2)
#     list1.append(3)
#     list1.append(4)
#     list1.append(5)
#     print("添加元素append:",list1)
#
#     # 插入元素(效率低下)    insert(place,obj)
#     list1.insert(0,90)
#     print("在指定位置插入元素:",list1)
#
#     # 修改(替换修改)元素      list[索引的下标数字num] = obj
#     list1[1] = 7
#     list1[0] = 8
#     list1[len(list1)-1] = 9
#     print("修改元素(索引修改):",list1)
#
#
#     #  删除元素   remove(obj)
#     list1.remove(4)
#     print("删除元素(remove删除):",list1)
#
#     # 元素查找(返回指定元素的索引下标)   index(obj,serial)   obj：要查找的元素   serial:有多个相同的元素时返回地serial个元素
#     A = list1.index(7)
#     print("下标为:",A)
#
# if __name__ == "__main__":
#     main()

