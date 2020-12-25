# -*- encoding:utf-8 -*-

"""
Function: 模型文件，放置DAO类，因为web部分实体关系简单，直接放一个模块
Create Time: 2020/12/25 16:43
Author: L1nf3ng
"""

from dashboard import db


# 作者类
class Author(db.Model):
    __tablename__ = "authors"
    name = db.Column(db.String(255))
    link = db.Column(db.String(255))
    create_time = db.Column(db.DateTime)
    id = db.Column(db.Integer, primary_key=True)
    # 创建一个属性记录属于他的文章
    posts = db.relationship("Post")

    # 重写输出函数，方便打印
    def __repr__(self):
        return "Class:{}<id{} name:{} link:{} create_time:{}>".format("Author", self.id, self.name, self.link,
                                                                     self.create_time)


# 文章类
class Post(db.Model):
    __tablename__ = "posts"
    title = db.Column(db.String(255))
    link = db.Column(db.String(255))
    tag = db.Column(db.String(60))
    datetime = db.Column(db.DateTime)
    origin = db.Column(db.String(60))
    id = db.Column(db.Integer, primary_key=True)
    # 外键名为 '表名.字段名'
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))

    # 重写输出函数，方便打印
    def __repr__(self):
        return "Class:{}<id{} title:{} link:{} tag:{} datetime:{} origin:{}>".format("Post", self.id, self.title,
                                                                                    self.link, self.tag, self.datetime,
                                                                                    self.origin)
