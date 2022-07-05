#log日志
"""
log日志可以用来记录错误、登录等信息

log日志实现的一般步骤:
    1.创建logger对象
    2.创建handle，用于写log日志的文件
    3.创建handle，用于在控制台上显示
    4.定义handle的输出格式
    5.将logger对象添加到handle中

log日志的记录等级(等级依次递增):
    debug:详细的信息通常只出现在诊断上（等级最低）
    info:确认一切预期进行
    warning:发生了一些意想不到的事
    error:一个严重的错误，可能没执行某些功能
    critical:一个严重的错误，程序可能无法运行（等级最高）

# 定义三种日志输出格式
standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

"""
import logging
#1.创建logger对象
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)               #log等级总开关，用于设置log日志记录的最低等级，设置该开关后只会记录此开关等级以上的日志

#2.创建handle，用于写log文件
logfile_name = "log.txt"
log_file = logging.FileHandler(logfile_name,mode="a")   #mode:log日志文件的写入模式
log_file.setLevel(logging.WARNING)                      #log_file等级控制开关

#3.创建handle，用于控制台显示
log_show = logging.StreamHandler()
log_show.setLevel(logging.CRITICAL)                        #log_show等级控制开关

#4.自定义log日志的输出格式
formatter = logging.Formatter("%(asctime)s-->%(filename)s[Line:%(lineno)d]-->%(levelname)s")
log_file.setFormatter(formatter)                        #log文件的输出格式
log_show.setFormatter(formatter)                        #log显示的输出格式

#5.将handle添加到logger中
logger.addHandler(log_file)
logger.addHandler(log_show)

#6.添加日志记录
logger.debug("This is Debug!")
logger.info("This is Info!")
logger.warning("This is Warning!")
logger.error("This is Error!")
logger.critical("This is Critical!")
