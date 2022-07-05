#   正则表达式(字符串匹配)
"""
    注意:
        在说明时用[]括起来的参数可有可无

    当想匹配某些特殊的字符时 如: 点.  问号?  可以在正则表达式中使用反斜杠 \ 实现转义 如:\.   \?
    re模块实现 result = re.match(正则表达式，要匹配的字符串)
                result.group()   匹配的结果(group返回一个字符串列表)
    规则:
        1)匹配一个字符
            .   :匹配任意一个字符(除换行\n外)       可使用re.match(正则表达式，要匹配的字符串,re.S) 让。匹配到空格
            [范围一，范围二,范围N]   :匹配范围一，范围二，范围N内的任意一个字符
            \d  :匹配一个数字，相当于[0-9]
            \D  :匹配一个非数字
            \s  :匹配一个空格或Tab
            \S  :匹配一个非空格或Tab
            \w  :匹配一个字符也可匹配中文和其它语言的文字    以英文为例相当于[A-Za-Z0-9_]  (解释:匹配A到Z 或 a到z 或 0到9 或 _ 中的任一个字符)
            \W  :匹配一个非字符

        2)匹配多个字符
            {num1,num2}     :前一个字符匹配num1到num2个      eg: \d{1,3}   匹配前1到3个数字
            {num}           :前一个字符匹配的个数大于等于num个     eg：\d{4}    匹配前4个数字
            ？              :前一个字符可有可无                   eg：[aA]?    a或A可有可无
            *               :前一个字符匹配0到N个(可以匹配空字符串)         eg：re.match(r".*","")  有匹配结果
            +               :前一个字符匹配1到N个(不可以匹配空字符串)        eg：re.match(r".+","")  无匹配结果

        3)匹配开头结尾
            ^       :匹配开头(python默认匹配开头)
            $       :匹配结尾，当正则表达式结束时字符串结束

        正则表达式的标准写法  :   re.match(r"^正则表达式$","字符串"[，re.S])

        4)正则表达式的分组使用小括号()实现
            eg:ret = re.match(r"^(\d*)(\D*)$","1111aaaa")
                ret.group(0)    结果:1111
                ret.group(1)    结果:aaaa
                        选择匹配:使用|实现     eg: (163|162)   代表匹配163或162     (^\)匹配到非斜杆
            注意正则表达式的分组可以在正则表达式内部引用，也可给分组命名并引用:
                eg：1.直接引用
                      re.match(r"<\w*>.*<\1>"，"<ha>aaa<ha>")                     结果:   <ha>aaa<ha>
                      re.match(r"<\w*><\w*>.*<\2><\1>","<ha1><ha2>aaa<ha2><ha1>")               结果:  <ha1><ha2>aaa<ha2><ha1>
                    2.命名引用
                        (?P<name>表达式)     命名
                        (?P=p1)              引用
                        re.match(r"<(?P<p1>\w*)>.*<(?P=p1)>","<ha1>aaa<ha1>")        结果:<ha1>aaa<ha1>

        5)正则表达式的其他使用方法及函数
            re.search()   在字符串当中匹配第一个符合正则表达式的字符串
                            eg:re.search(r"\d+","播放量:2234,点击量:7777")   返回:2234
            re.findall()  在字符串当中匹配所有符合(正则表达式)要求的字符串"
                            eg:re.findall(r"\d+","播放量:2234,点击量:7777")  返回:[2234,7777]
            re.sub()       寻找所有符合的字符串并替换(可以替换成函数的的使用)
                            eg:1)re.sub(r"\d+","111","fasd:123,hjk:09090")    返回:(fasd:111,hjk:111)
                                2)说明add函数需要自行编写实现，在此不加编写
                                    add函数实现加1的功能
                                    re.sub(r"\d+",add,"a:2,h:90")         返回:(a:3,h:91)
            re.split()    实现字符串匹配切割操作
                            eg:re.split(r":","abc:def")                     返回:[abc,def]



"""
import re

"""1)匹配单个字符"""
# def main():
#     #   1.匹配一个数字
#     result1 = re.match(r"\d","7")
#     print("result1:",result1.group())
#     #   2.匹配一个非数字
#     result2 = re.match(r"\D", "a")
#     print("result2:", result2.group())
#
#     #   3.匹配一个空格或Tab
#     result3 = re.match(r"\s","  ")
#     print("result3:",result3.group(),"空格结束")
#     #   4.匹配一个非空格或Tab
#     result4 = re.match(r"\S","G")
#     print("result4:",result4.group())
#
#     #   5.匹配一个任意字符(包括换行)
#     result5 = re.match(r".","&")
#     print("result5:",result5.group())
#
#     #   6.范围匹配
#     result6 = re.match(r"[0-36-7]","3")
#     print("result6:",result6.group())
#
#     result7 = re.match(r"[a-zA-Z0-9_]","_")
#     print("result7:",result7.group())
#
#     result8 = re.match(r"[a-zA-Z0-9_]", "A")
#     print("result8:", result8.group())
#
# if __name__ == "__main__":
#     main()


"""2)匹配多个字符"""
# def main():
#     #   1.{m,n}匹配
#     result1 = re.match(r"\d{3,5}","12345678")
#     print("result1:",result1.group())
#
#     #   2.{n}匹配
#     result2 = re.match(r"[a-z]{3}","abcdf")
#     print("result3:",result2.group())
#
#     #   3.?匹配
#     result3 = re.match(r"_?","a")
#     print("result3:",result3.group())
#
#     #   4.+匹配
#     result4 = re.match(r"[a-zA-Z]+","")
#     try:
#         print("result4:",result4.group())
#     except:
#         print("result4匹配无结果")
#
#     #   5.*匹配
#     result5 = re.match(r".*","""fas
#                                 fasdf
#                                 1231
#                                 $@$!$(&(
#                                 gsdf""",re.S)
#     print("result5:",result5.group())
#
#
#
# if __name__ == "__main__":
#     main()


"""3)开头结尾匹配"""
# def main():
#     #   正好匹配11个数字
#     result1 = re.match(r"^\d{11}$","15572825267")
#     print("result1匹配成功:",result1.group())
#
#     result = re.match(r"^[a-zA-Z0-9]*_$","fda353_")
#     print("result匹配成功:",result.group())
#
#     #   匹配失败
#     result2 = re.match(r"^\d{3}$","15572825267")
#     try:
#         print("result2匹配成功:",result2.group())
#     except:
#         print("result2匹配失败")
#
#
# if __name__ == "__main__":
#     main()



"""4)分组"""


#A.分组选择匹配
# result1 = re.match(r"(163|162)","163")
# result2 = re.match(r"(162|163)","162")
# print("result1:{0}\t\tresult2:{1}".format(result1.group(),result2.group()))

#B.分组直接引用
# result = re.match(r"<(\w*)><(\w*)>.*<\2><\1>","<ha1><ha2>aaa<ha2><ha1>")
# print(result.group())

#C.分组命名引用
# result = re.match(r"<(?P<p1>\w*)>.*<(?P=p1)>","<ha1>aaa<ha1>")
# print(result.group())




"""5)高级用法及函数"""


#A. re.search()
# result = re.search(r"\d+","point:123,brost:333")
# print(result.group())

#B. re.findall()
# result = re.findall(r"\d+","point:123,brost:333")
# print(result)

#C. re.split()
# result = re.split(r":","aaa:bbb:ccc:ddd")
# print(result)



"""邮件匹配"""
def main():
    def match(matcher):
        result = re.match(r"^[a-zA-Z0-9]{4,20}@(163|162|qq|gmail|outlook)\.com$",matcher)
        if result:
            return result
        else:
            return None

    mail_list = ["asdf$",
                 "1234@asdf.com",
                 "12345@qq.com",
                 "827349fsdf@outlook.com"]
    for matcher in mail_list:
        result = match(matcher)
        if result:
            print("合法邮箱:",matcher)
        else:
            print("非法邮箱:",matcher)

if __name__ == "__main__":
    main()