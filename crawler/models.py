# -*- encoding:utf-8 -*-

"""
Function: 爬虫部分使用的基本类
Create Time: 2020/12/26 20:38
Author: L1nf3ng
"""

import datetime
import re
import uuid

import aiohttp
from lxml import etree
from dashboard.models import Post

"""
# 文章类，记录标题、链接、作者、分类、发布日期等重要信息
class Article:
    # python的特性：只能定义一个构造函数，后期可以用*args的长度改造一下
    # 构造函数改为列表初始化：[title, link, author, category, date, origin]
    def __init__(self, data):
        self._title= data[0]
        self._href= data[1]
        self._author=  data[2]
        self._author_link = data[3]
#        self._type= data[4] if type(data[4])==str else "Unknown"
        self._type = data[4]
        self._date= self.handle_date(data[5])
        self._origin = data[6]
        if not self._href.startswith('https://') and not self._href.startswith('http://'):
            self._href = self._origin + self._href
        if not self._author_link.startswith('https://') and not self._author_link.startswith('http://'):
            self._author_link = self._origin + self._author_link

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def author_link(self):
        return self._author_link

    @property
    def tag(self):
        return self._type

    @property
    def link(self):
        return self._href

    @property
    def date(self):
        return self._date

    # in this func, we adjust the date-time into '%y-%m-%d' form
    def handle_date(self,date):
        ymd = re.search('(\d+)[-年](\d+)[-月](\d+)日?',date)
        # 非常规格式，全部转成当天
        if ymd is None:
            return today()
        year,month,day = ymd.groups()
        return year+'-'+month+'-'+day

    # 输出函数，要么重载，要么自写。输出格式到文件，按模板形式输出为html、csv等
    def __repr__(self):
        return "Post informaiton:\nTitle:{}\n Author:{} Type:{} Date:{} Link: {}\n".\
            format(self._title,self._author,self._type,self._date,self._href)

    # 将元数据化为字典，再转成json字符串，方便与其他服务交互
    # 暂时未用到
    def jsonify(self):
        input= {'title':self.title, 'author':self.author, 'tag':self.tag, 'link':self.link, 'date':self.date}
        return json.dumps(input)
"""


# 目标类，记录目标的爬取指标：链接、解析时的xpath语法
# Target中的表达式数组分别代表（post位置，标题位置、链接位置、作者位置、分类位置、日期位置）
# Target中的坏表达式列表代表要删除的节点，因为这些某些节点的存在该绕了正常的解析过程，所以先找到它们，并删除掉
# ！！！！注意，删除的是找到节点的父节点 ！！！！
class Target:
    def __init__(self, url, good_xpath, bad_xpath=None):
        self._url = url
        self._expr = []
        self._expr.extend(good_xpath)
        self._bad_expr = bad_xpath

    @property
    def url(self):
        return self._url

    @property
    def expr(self):
        return self._expr

    @property
    def bad_expr(self):
        return self._bad_expr


# 收集器类，负责测试连接、请求、解析文档、处理异常等
class Collector:
    def __init__(self, target, proxy= False):
        self._target = target
        self._headers = { "User-Agent":"Mozilla/5.0 Chrome/72.0.3626.121 Safari/537.36" }
#                          "Accept":"text/html,application/xhtml+xml,application/xml",
#                          "Accept-Encoding": "gzip, deflate, br",
#                          "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8" }
        self._proxy = "http://127.0.0.1:8080"
        # set_proxy label shows whether turn on the proxy
        self._set_proxy = proxy
        # default charset is utf-8
        self._charset = 'utf-8'
        # the time zone which we acutually need
        self._time_zone = self.define_scope()
        self._posts = []

    def define_scope(self):
        scope = []
        now = datetime.datetime.now()
        scope.append(now.strftime("%Y-%m-%d"))
        week = now.strftime("%a")
        # 如果今天是周一，则顺便爬取上周末的文章
        if week == "Mon":
            last = now - datetime.timedelta(days=1)
            scope.append(last.strftime("%Y-%m-%d"))
            last = now - datetime.timedelta(days=2)
            scope.append(last.strftime("%Y-%m-%d"))
        return scope

    # 为了调高效率，一个站内的url应当尽可能使用一个session；不同的站使用不同session
    async def get_blog(self):
        async with aiohttp.ClientSession() as session:
#            if self._set_proxy:
#                params = {'headers':self._headers, 'proxy':self._proxy}
#            else:
#                params = {'headers':self._headers}
            async with session.get(self._target.url, headers= self._headers, verify_ssl=False) as resp:
                if resp.status !=200:
                    print('Cannot connect {} just now. Try it later or check the network...'.format(self._target.url))
                    return None
                return await resp.text()

    def parse_blog(self, blog):
        doc = etree.fromstring(blog, etree.HTMLParser())
#        doc = etree.parse(blog, p)
        # last expr defines the rule to delete useless tags
        if self._target.bad_expr!=None:
            for primitive in self._target.bad_expr:
                for tag in eval('doc.'+primitive):
                    super_tag = tag.getparent().getparent()
                    super_tag.getparent().remove(super_tag)
        # 1st expr determines the articles elements
        posts = eval('doc.'+self._target.expr[0])
        # left expressions determine posts information
        debug_num = 0
        Wrong_Handle = False
        for post in posts:
            data = []
            for od in range(1, len(self._target._expr), 1):
                # 对od语句的解析时很核心的
                try:
                    if self._target.expr[od]=="":
                        data.append("unkown")
                    elif "regex" in self._target.expr[od]:
                        xpathExpression, reExpression = self._target.expr[od].split(",")
                        result = eval('post.' + xpathExpression)
                        pattern = reExpression.split(":")[1].strip().strip("'")
                        m = re.search(pattern, result, re.S)
                        data.append(m.group(2))
                    else:
                        try:
                            result = eval('post.' + self._target.expr[od])
                            result = str(result)
                        except:
                            result = "unkown"
                        data.append(result.strip())
                except Exception as ext:
                    # when exception occurs, store the doc into a file to check later
                    if Wrong_Handle == True:
                        pass
                    else:
                        print(ext,': post number {}, the expression {} errors!'.format(debug_num, od))
                        print("The expression : %s" % 'post.'+ self._target.expr[od])
                        print("Exception Context: \n{}".format(eval('post.tostring()')))
                        print("The Current expr is: "+ self._target.expr[od])
                        filename = '{}_2_parse.html'.format(str(uuid.uuid1()))
                        with open(filename,'w', encoding= 'utf8') as file:
                            file.write(blog)
                        print('we store it in {}'.format(filename))
                        data.append("无")
                        Wrong_Handle = True

            debug_num += 1
            data.append(self._target.url)
            article = Post(data)
            # we only add the post in the time zone.
            if article.date in self._time_zone:
                self._posts.append(Post(data))

    @property
    def posts(self):
        return self._posts

