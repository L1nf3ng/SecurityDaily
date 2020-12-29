# -*- encoding:utf-8 -*-

"""
Function: 模型文件，放置DAO类，因为web部分实体关系简单，直接放一个模块
Create Time: 2020/12/25 16:43
Author: L1nf3ng
"""

from dashboard import db
from crawler import dateTimeFormatter

# 作者类
class Author(db.Model):
    __tablename__ = "authors"
    name = db.Column(db.String(255))
    link = db.Column(db.String(255))
    create_time = db.Column(db.Date)
    id = db.Column(db.Integer, primary_key=True)
    # 创建一个属性记录属于他的文章
    posts = db.relationship("Post", back_populates="author")

    def __init__(self, link, name):
        self.link = link
        self.name = name
        self.create_time = None

    @dateTimeFormatter
    def setCreateTime(self, date=None):
        self.create_time = date

    # 重写输出函数，方便打印
    def __repr__(self):
        return "Class:{}<id:{} name:{} link:{} create_time:{}>".format("Author", self.id, self.name, self.link,
                                                                     self.create_time)


# 文章类
class Post(db.Model):
    __tablename__ = "posts"
    title = db.Column(db.String(255))
    link = db.Column(db.String(255))
    tag = db.Column(db.String(60))
    datetime = db.Column(db.Date)
    origin = db.Column(db.String(60))
    id = db.Column(db.Integer, primary_key=True)
    # 外键名为 '表名.字段名'
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))
    # 创建一个属性代表它的作者对象
    author = db.relationship("Author", back_populates = "posts")

    def __init__(self, title, link, tag, origin, author):
        self.title = title
        self.link = link
        self.tag = tag
        self.origin = origin
        self.datetime = None
        self.author = author
        if isinstance(author, Author):
            self.author_id = author.id
        else:
            # 抛出异常
            raise Exception(TypeError)

    @dateTimeFormatter
    def setDateTime(self, date=None):
        self.datetime = date

    # 重写输出函数，方便打印
    def __repr__(self):
        return "Class:{}<id:{} title:{} link:{} tag:{} datetime:{} origin:{}>".format("Post", self.id, self.title,
                                                                                    self.link, self.tag, self.datetime,
                                                                                    self.origin)
