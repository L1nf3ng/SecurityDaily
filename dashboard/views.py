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
from flask import request, render_template, redirect, url_for, jsonify


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


# 分页展示结果
@app.route('/show', methods=['GET'])
def show():
    # 默认第一页并只显示10条数据
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 15, type=int)
    # 查询爬取数据
    pagination = db.session.query(Post).order_by(Post.datetime.desc()).paginate(page, per_page)
    # 注意返回响应时的字符编码问题
    return render_template("report.html", date=today(), pagination= pagination)


@app.route("/articles/list", methods=["GET"])
def getAllPosts():
    posts = db.session.query(Post).order_by(Post.datetime.desc()).all()
    ret = []
    for post in posts:
        ret.append({
            "id": post.id,
            "title": post.title,
            "description": post.author.name,
            "content": post.summary
        })
    s= 9
    return jsonify(ret)


# 错误处理之404
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


# 错误处理之500
@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500


# app.add_url_rule('/', view_func=config)
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# @app.route("/")
# def index():
#     return redirect(url_for("config"))


@app.route("/start-htr-hunter", methods=['GET'])
def start_htr_hunter():
    #TODO: 1.调用huntr接口获取文档内容。
    #
    # TODO：2.调用千文turbo模型进行内容总结

    # TODO：3.结果存储mongo并返回展示。

    # TODO：4.做频次限制，一天一次。
    pass
