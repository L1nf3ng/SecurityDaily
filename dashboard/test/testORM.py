# -*- encdoing:utf-8 -*-

import unittest

from datetime import datetime
from dashboard import db
from dashboard.models import Author, Post


class MyTestCase(unittest.TestCase):

    def init_db_data(self):
        # add one writer
        author = Author(name="rivative", link="http://www.anquanke.com/author/3432523", create_time=datetime.utcnow())
        db.session.add(author)

        # add two posts belongs to him
        post1 = Post(title="sword to offer", link="https://www.douban.com/1324", tag="society", datetime = datetime.utcnow(), origin="websource", author_id="1")
        post2 = Post(title="whoever calls is dead", link="https://www.baidu.44342.com/1324", tag="fiction", datetime=datetime.utcnow(),
                     origin="horour", author_id="1")
        db.session.add(post1)
        db.session.add(post2)
        post3 = Post(title="生死有命", link="https://www.aliyun.com/1324", tag="小说", datetime=datetime.utcnow(), origin="巴比伦", author_id="1")
        db.session.add(post3)
        db.session.commit()

    def test_orm(self):
        # self.init_db_data()
        row1 = db.session.query(Author).filter_by(id=1).one()
        for post in row1.posts:
            print(post)
        # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
