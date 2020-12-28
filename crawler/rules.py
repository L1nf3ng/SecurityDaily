# -*- encoding:utf-8 -*-

"""
Function: 
Create Time: 2020/12/28 16:21
Author: L1nf3ng
"""

# expr顺序对应意义：
#           0-->    post位置
#           1-->    标题位置
#           2-->    链接位置
#           3-->    作者位置
#           4-->    作者信息链接
#           5-->    分类位置
#           6-->    日期位置
#               干扰项规则，用来删除干扰节点，因为可能不止一项，
ORIGIN_RULES = {
    "xianzhi": {
        "standard": ["xpath('//article')",
                     "xpath('./header/h5/a')[0].text",
                     "xpath('./header/h5/a/@href')[0]",
                     "xpath('./section')[0].text, regex: '(作者|译者)：([^\n]+)\n'",
                     "",  # 作者信息链接
                     "xpath('./header/section[1]/a')[0].text",  # 分类位置
                     "xpath('./header/section[1]/span/time[@class=\\'fulldate\\']')[0].text"], # 日期位置
        "filter": ""
    },
    "anquanke": "https://www.anquanke.com",
    "freebuf": "https://www.freebuf.com",
    "sihou": "https://www.4hou.com",
    "seebug": "https://paper.seebug.org"
}


seebug = Target("https://paper.seebug.org", )  # 日期位置

aliyun = Target('https://xz.aliyun.com', ["xpath('//td')",
                                          "xpath('./p[1]/a[@class=\\'topic-title\\']')[0].text",
                                          "xpath('./p[1]/a[@class=\\'topic-title\\']/@href')[0]",
                                          "xpath('./p[2]/a[1]')[0].text",
                                          "xpath('./p[2]/a[1]/@href')[0]",
                                          "xpath('./p[2]/a[2]')[0].text",
                                          "xpath('./p[2]/text()')[2]"])

anquanke = Target('https://www.anquanke.com', ["xpath('//div[@class=\\'article-item common-item\\']')",
                                               "xpath('.//div[@class=\\'title\\']/a')[0].text",
                                               "xpath('.//div[@class=\\'title\\']/a/@href')[0]",
                                               "xpath('.//div[@class=\\'article-info-left\\']/a/span')[0].text",
                                               "xpath('.//div[@class=\\'article-info-left\\']/a/@href')[0]",
                                               "xpath('.//div[@class=\\'tags  hide-in-mobile-device\\']/a/div/span')[0].text",
                                               "xpath('.//div[@class=\\'article-info-left\\']/span/span/i')[0].tail"])

freebuf = Target('https://www.freebuf.com',
                 ["xpath('//div[@class=\\'article-list\\']//div[@class=\\'article-item\\']')",  # POST位置
                  "xpath('./div/div/a/span')[0].text",  # 标题位置
                  "xpath('./div/div/a/@href')[0]",  # 链接位置
                  "xpath('./div[2]/div/div/p/a/span[2]')[0].text",  # 作者位置
                  "xpath('./div[2]/div/div/p/a/@href')[0]",  # 作者详情
                  "xpath('./div[2]/a/p/span')[0].text",  # 分类位置
                  "xpath('./div[2]/div/div/p[2]/span')[0].text"],  # 日期位置
                 ["xpath('//div[@class=\\'article-list\\']//div[@class=\\'article-item\\']/div/span')",  # 排除项
                  "xpath('//div[@class=\\'column-carousel\\']')"])

_4hou = Target('https://www.4hou.com', ["xpath('//div[@id=\\'new-post6\\']')",
                                        "xpath('.//div[@class=\\'new_con\\']/a/h1')[0].text",
                                        "xpath('.//div[@class=\\'new_con\\']/a/@href')[0]",
                                        "xpath('.//div[@class=\\'avatar_box newtime\\']/a/p')[0].text",
                                        "xpath('.//div[@class=\\'avatar_box newtime\\']/a/@href')[0]",
                                        "xpath('.//div[@class=\\'new_img\\']/span')[0].text",
                                        "xpath('.//div[@class=\\'avatar_box newtime\\']/span')[0].text"])
