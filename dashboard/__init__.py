# -*- encoding:utf-8 -*-

import os

from flask import Flask, request, render_template


def create_app(test_env_config=None):

    # app = Flask(__name__, instance_relative_config=True)
    app = Flask(__name__)
    app.config.from_mapping(
        # 本例中web的默认配置，可通过这里的字典参数配置
        # SECRET_KEY="dev",

        # 数据库链接配置
        # DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_env_config is None:
        # 开发环境下，使用config.py文件配置（存在的情况下）
        app.config.from_pyfile("config.py", silent=True)
    else:
        # 测试环境下，通过参数确定配置文件目录
        app.config.update(test_env_config)


    # 配置视图函数
    @app.route("/config", methods=['GET', 'POST'])
    def config():
        if request.method == 'GET':
            return render_template()
        else:
            return "Hello, World!"


    @app.route('/show', methods = 'GET')
    def show():
        return 'some page lists'


    @app.route("/favicon.ico")
    def favicon():
        return app.send_static_file('favicon.ico')

    return app
