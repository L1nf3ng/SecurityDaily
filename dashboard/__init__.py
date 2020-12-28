# -*- encoding:utf-8 -*-

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# 定义一些常量
LOGS_FOLDER = "logs"

# app = Flask(__name__, instance_relative_config=True)
app = Flask(__name__)

# 开发环境下，使用config.py文件配置（存在的情况下）
app.config.from_pyfile("config.py", silent=True)

# 在运行时创建日志文件存放日志
try:
    os.makedirs(LOGS_FOLDER)
except OSError:
    pass

# 初始化数据库源
db = SQLAlchemy(app)

from dashboard import views,config,models
