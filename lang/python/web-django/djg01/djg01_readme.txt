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

