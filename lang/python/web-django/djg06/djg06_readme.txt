1.ajax实现页面的部分刷新(异步)

2.cookie在浏览器(客户端)保存用户信息（request.COOKIES字典）
    设置cookie:
        #   在views.py中的函数
        def set_cookie(request):
            response = HttpResponse(回传浏览器的数据)        #  设置返回数据
            response.set_cookie(key,value,max_age)          #   key:在cookie字典中的键(key)   value:在cookie字典中的值(value)   max_age:存储的最长时间，单位为秒
            return response                                 #   返回数据
    读取cookie:
        #   在views.py中的函数
        def get_cookie(request):
            变量名 = request.COOKIES[cookie数据的key]
            return HttpResponse(回传浏览器的数据)
    清除cookie:
        在浏览器的设置中清除cookie数据

3.session在服务器保存用户信息,session数据存储在django_session数据表中（request.session字典）
    设置session数据:
        def set_session(request):
            request.session[session字典的键] = 值
            return HttpResponse(回传浏览器的数据)
    获取session数据:
        def get_session(request):
            变量名 = request.session["所需数据的key"]
            return Httpresponse(回传浏览器的数据)
    清除session数据:
        def del_session(request):
            #   清除某条数据
            del request.session[某条数据的key]
            #   逻辑删除所有数据
            request.session.clear()
            #   全部彻底删除所有session数据
            request.session.flush()
