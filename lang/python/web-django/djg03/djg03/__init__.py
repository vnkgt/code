import pymysql                                  #   pysql需要通过pip安装
pymysql.version_info=(1,3,13,"final",0)         #   解决django与MySQLdb不匹配的问题，有时可以不写
pymysql.install_as_MySQLdb()                    #   保证在django能够使用MySQLbd
