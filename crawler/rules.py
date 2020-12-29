# -*- encoding:utf-8 -*-

"""
Function: xpath解析规则定义文件，也可以使用json文件，后期可能会支持
TODO: 支持上传json文件定义规则（一种扩展方式）
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
#           filter-->   干扰项规则，用来删除干扰节点，因为可能不止一项，
ORIGIN_DICT = {

    "xianzhi": {
        "origin": "https://xz.aliyun.com",
        "standard": ["xpath('//td')",            # post <div>的位置
                      "xpath('./p[1]/a[@class=\\'topic-title\\']')[0].text",  # 标题位置
                      "xpath('./p[1]/a[@class=\\'topic-title\\']/@href')[0]", # 链接位置
                      "xpath('./p[2]/a[1]')[0].text",    # 作者位置
                      "xpath('./p[2]/a[1]/@href')[0]",   # 作者信息链接
                      "xpath('./p[2]/a[2]')[0].text",   # 分类位置
                      "xpath('./p[2]/text()')[2]"],    # 日期位置
        "filter": ""
    },

    "anquanke": {
        "origin":"https://www.anquanke.com",
        "standard": ["xpath('//div[@class=\\'article-item common-item\\']')",            # post <div>的位置
                   "xpath('.//div[@class=\\'title\\']/a')[0].text",      # 标题位置
                   "xpath('.//div[@class=\\'title\\']/a/@href')[0]",      # 链接位置
                   "xpath('.//div[@class=\\'article-info-left\\']/a/span')[0].text",      # 作者位置
                   "xpath('.//div[@class=\\'article-info-left\\']/a/@href')[0]",          # 作者信息链接
                   "xpath('.//div[@class=\\'tags  hide-in-mobile-device\\']/a/div/span')[0].text",   # 分类位置
                   "xpath('.//div[@class=\\'article-info-left\\']/span/span/i')[0].tail"],           # 日期位置
        "filter":""
    },

    "freebuf":{
        "origin":"https://www.freebuf.com",
        "standard": ["xpath('//div[@class=\\'article-list\\']//div[@class=\\'article-item\\']')",  # POST位置
                  "xpath('./div/div/a/span')[0].text",  # 标题位置
                  "xpath('./div/div/a/@href')[0]",  # 链接位置
                  "xpath('./div[2]/div/div/p/a/span[2]')[0].text",  # 作者位置
                  "xpath('./div[2]/div/div/p/a/@href')[0]",  # 作者详情
                  "xpath('./div[2]/a/p/span')[0].text",  # 分类位置
                  "xpath('./div[2]/div/div/p[2]/span')[0].text"],  # 日期位置
        "filter":  ["xpath('//div[@class=\\'article-list\\']//div[@class=\\'article-item\\']/div/span')",  # 排除项
                  "xpath('//div[@class=\\'column-carousel\\']')"]
    },

    "sihou": {
        "origin":"https://www.4hou.com",
        "standard":["xpath('//div[@id=\\'new-post6\\']')",           # POST位置
                    "xpath('.//div[@class=\\'new_con\\']/a/h1')[0].text",    # 标题位置
                    "xpath('.//div[@class=\\'new_con\\']/a/@href')[0]",  # 链接位置
                    "xpath('.//div[@class=\\'avatar_box newtime\\']/a/p')[0].text",    # 作者位置
                    "xpath('.//div[@class=\\'avatar_box newtime\\']/a/@href')[0]",  # 作者详情
                    "xpath('.//div[@class=\\'new_img\\']/span')[0].text",     # 分类位置
                    "xpath('.//div[@class=\\'avatar_box newtime\\']/span')[0].text"]   # 日期位置
    },

    "seebug": {
        "origin": "https://paper.seebug.org",
        "standard": ["xpath('//article')",  # post <div>的位置
                     "xpath('./header/h5/a')[0].text",  # 标题位置
                     "xpath('./header/h5/a/@href')[0]",  # 链接位置
                     "xpath('./section')[0].text, regex: '(作者|译者)：([^\n]+)\n'",  # 作者位置
                     "",  # 作者信息链接
                     "xpath('./header/section[1]/a')[0].text",  # 分类位置
                     "xpath('./header/section[1]/span/time[@class=\\'fulldate\\']')[0].text"],  # 日期位置
        "filter": ""
    }
}
