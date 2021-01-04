# -*- encoding:utf-8 -*-

"""
Function: 包括数据库连接等信息
Create Time: 2020/12/23 10:29
Author: L1nf3ng
"""

DATABASE_TYPE = "mysql"    # or "sqlite"

########################################################
#
#                   SQLite3数据库配置
#
########################################################

SQLALCHEMY_DATABASE_URI_SQLITE = "sqlite:///../SecurityDaily.db"


########################################################
#
#                   MySQL数据库配置
#
########################################################

# 远程/本地MySQL服务器的IP
HOST = "192.168.40.62"
# 远程/本地MySQL服务器的端口
PORT = 3306
# MySQL账户名称
USERNAME = 's_d'
# MySQL连接密码
PASSWORD = '112233'
# 不建议修改，如修改请和sql脚本一同修改
DATABASE = 'SecurityDaily'

SQLALCHEMY_DATABASE_URI_MYSQL = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME, PASSWORD, HOST, PORT, DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False
