# -*- encoding:utf-8 -*-

"""
Function: 包括数据库连接等信息
Create Time: 2020/12/23 10:29
Author: L1nf3ng
"""

# HOST = '10.0.12.93'
HOST = "192.168.40.62"
PORT = 3306
USERNAME = 's_d'
PASSWORD = '112233'
DATABASE = 'SecurityDaily'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
