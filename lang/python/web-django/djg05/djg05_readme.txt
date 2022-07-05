获取html中传输过来的POST数据

http协议中的数据传输方式:
    POST:提交的参数在http请求头。安全性更高
    GET:提交的参数在url请求的地址中,数据放在url地址中

#   request是QueryDict对象
#   QueryDict属性与字典相似
#   在python manage.py shell中运行以下代码
# q = QueryDict("a=1&b=2&c=3")
# q.get('a')
# q.get('b')
#
# q1 = QueryDict("a=1&a=2&a=3")
# q1.getlist('a')


post相当于一个字典:
    eg:在views中
        获取post中的一个数据:
            def index(request):
                name = request.POST.get("name")     #   获取POST中名为"name"的参数
                age_list = request.POST.getlist("age")  #   POST中有多个"age"参数时,使用getlist,返回一个列表

