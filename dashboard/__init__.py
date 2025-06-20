# -*- encoding:utf-8 -*-

import os
import time
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# 自写的logger初始化函数，功能没有网上的全，但本项目够用
def initLogger():
    LOGDIR='./logs/'
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logFileName = LOGDIR + time.strftime('%Y%m%d')+ '.log'
    fileHandler = logging.FileHandler(filename=logFileName, encoding='utf8')
    fileHandler.setFormatter(logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"))
    logger.addHandler(fileHandler)
    return logger


# 定义一些常量
LOGS_FOLDER = "logs"

# app = Flask(__name__, instance_relative_config=True)
app = Flask(__name__, static_folder='./static')

# 开发环境下，使用config.py文件配置（存在的情况下）
app.config.from_pyfile("config.py", silent=True)
if app.config["DATABASE_TYPE"] == "sqlite":
    app.config["SQLALCHEMY_DATABASE_URI"] = app.config["SQLALCHEMY_DATABASE_URI_SQLITE"]
elif app.config["DATABASE_TYPE"] == "mysql":
    app.config["SQLALCHEMY_DATABASE_URI"] = app.config["SQLALCHEMY_DATABASE_URI_MYSQL"]

# 在运行时创建日志文件存放日志
try:
    os.makedirs(LOGS_FOLDER)
except OSError:
    pass

# 初始化数据库源
db = SQLAlchemy(app)
# 因为web端先启动，所以由它完成logger初始化
logger = initLogger()


# from dashboard import views,config,models


