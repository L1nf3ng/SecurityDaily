# -*- encoding:utf-8 -*-

"""
Function: 
Create Time: 2020/12/24 20:35
Author: L1nf3ng
"""

from dashboard import app, db
# 引入Model类
from dashboard.models import Author, Post
from flask import request, render_template


# 配置视图函数
@app.route("/config", methods=['GET', 'POST'])
def config():
    if request.method == 'GET':
        return render_template()
    else:
        return "Hello, World!"


# 配置结果展示试图
@app.route('/show', methods = ['GET'])
def show():

    # 查询数据
    # 暂不写分页信息
    author = db.session.query(Author).filter_by(id=1).one()
    print(author)
    return "go check database!"
    # return author


@app.route("/favicon.ico")
def favicon():
    return app.send_static_file('favicon.ico')

