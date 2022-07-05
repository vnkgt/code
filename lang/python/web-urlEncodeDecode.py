#url请求的编码与解码
"""
浏览器传回的http数据中
    不允许出现中文、特殊符号，若有中文或特殊符号则浏览器会自动使用url编码进行重新编码

使用url编码解码:
    import urllib.parse
    urllib.parse.quote(要编码的字符串)         ----->url编码
    urllib.parse.unquote(要解码的字符串)       ----->url解码
"""
import urllib.parse
#编码
a = urllib.parse.quote("中国")
print(a)
#解码
b = urllib.parse.unquote(a)
print(b)
