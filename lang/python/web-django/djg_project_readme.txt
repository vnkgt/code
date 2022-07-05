djg01
    1.创建django项目
        1.1.配置项目django的setting.py文件
            1.1.1.安装应用:INSTALLED_APPS列表添加应用名
            1.1.2.配置模板文件(html)所在的位置:TEMPLATES列表中的'DIRS'列表添加位置
        1.2.配置django的urls.py文件
            在urlpatterns列表中使用url(正则表达式,include函数或指定函数名)，添加urls处理的方法
    2.创建django应用
        2.1.models.py模型类使用
        2.2.admin.py后台管理使用
        2.3.创建urls的匹配文件(urls_handle.py)
        2.4.views.py视图使用
        2.5.模板文件使用(template下的html文件)

djg02
    1.显示“127.0.0.1:端口号/books”页面
    2.将books页面中的书名，在相应的html文件当中设置为链接标签
    3.点击books页面的书名转到，相应书名下的所有英雄名

djg03
    主要用于查询测试

djg04
    1.自关联表的查询
        models.py
    2.url参数的捕获
        urls_handel.py
        views.py

djg05
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

djg06
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

djg07
    1.模板语言
        模板变量
        for循环
        if判断
    2.模板过滤器
        内置过滤器
        自定义过滤器
    3.模板继承
    4.模板转义
    5.登录校验装饰器
        确定登录状态，才能修改密码
    6.html中防止csrf攻击

djg08
    1.url逆向解析
    2.html模板使用静态文件
        图片/js/css

djg09
    中间件的使用
        1)创建中间件的.py文件
        2)编写中间件类及函数
        3)setting.py注册中间件类

djg10
    0.自关联表的创建
        models.py
    1.模型类的后台管理
        models.py
        admin.py
    2.分页
    3.ajax省市县选择

djg11
    文件上传
        0)配置setting.py
            MEDIA_ROOT
        1)通过浏览器登录后台上传
            admin.py
            models.py
            static/media/Img_Admin
        2)通过浏览器客户上传
            template/temp/client_upload_html.html
            static/media/Img_Client



