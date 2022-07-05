#   filters.py的文件名可以是任意的文件名
#   自定义过滤器
#   过滤器其实就是python函数
from django import template
#   创建一个Library类的对象
register = template.Library()     # 只能叫register

# 至少有一个参数,最多传两个参数
#   传递一个参数
@register.filter(name="mod")    #   name参数:过滤器在html模板中使用时的名称
def mod(num):
    """判断是否为偶数"""
    return num%2==0

# 传递两个参数
def add(a,b):
    return a+b
register.filter(name="add")