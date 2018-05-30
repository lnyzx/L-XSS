import multiprocessing

bind = "127.0.0.1:8000"   #绑定的ip与端口
workers = 2                #核心数
#loglevel = 'debug'   #日志等级
proc_name = 'gunicorn_project'   #进程名
