# -*- encoding:utf-8 -*-

"""
Function: 爬虫基本功能函数
Create Time: 2020/12/22 15:23
Author: L1nf3ng
"""

import re
from functools import wraps
from datetime import datetime


ORIGIN_DICT = {
    "xianzhi":"https://xz.aliyun.com",
    "anquanke":"https://www.anquanke.com",
    "freebuf":"https://www.freebuf.com",
    "sihou":"https://www.4hou.com",
    "seebug":"https://paper.seebug.org"
}


# 日期格式的转换的装饰器
def dateTimeFormatter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 打包后的普通参数
        # 因为args参数可读不可写，所以这里要求日期通过`date=xxx`的形式传入

        # 键值对格式参数
        for (key, value) in kwargs.items():
            ymd = re.search('(\d+)[-年](\d+)[-月](\d+)日?', value)
            if ymd is not None:
                # 格式调整
                year, month, day = ymd.groups()
                kwargs[key] = year + '-' + month + '-' + day
            else:
                # 参数为空时默认赋值为当天日期
                kwargs[key] = year + '-' + month + '-' + day

        func(*args, **kwargs)
    return wrapper


def today():
    return datetime.now().strftime('%Y-%m-%d')


from crawler import utils
