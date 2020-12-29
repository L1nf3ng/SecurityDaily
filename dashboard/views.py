# -*- encoding:utf-8 -*-

"""
Function: 
Create Time: 2020/12/24 20:35
Author: L1nf3ng
"""

import asyncio
from dashboard import app, db
from crawler import today
# 引入Model类
from dashboard.models import Post
from crawler.utils import unit_task
from flask import request, render_template, redirect, url_for


# 配置视图函数
@app.route("/config", methods=['GET', 'POST'])
def config():
    if request.method == 'GET':
        return render_template("config.html")
    else:
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        loop = asyncio.get_event_loop()
        corutines = []
        # 根据复选框勾选的情况创建线程、分配任务、进行扫描
        for key in request.form.keys():
            # 创建任务
            corutines.append(unit_task(key))
        # 启动协程，运行直到全部结果返回
        loop.run_until_complete(asyncio.wait(corutines))
        loop.close()
        return redirect(url_for('show'))


# 配置结果展示试图
@app.route('/show', methods = ['GET'])
def show():
    # 查询爬取数据，暂不写分页功能
    posts = db.session.query(Post).all()
    # 注意返回响应时的字符编码问题
    return render_template("report.html", date=today(), posts=posts)


# 错速处理之404
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

app.add_url_rule('/', view_func=config)

