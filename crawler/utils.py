# -*- encoding:utf-8 -*-

"""
Function: 与任务有关的基本类
Create Time: 2020/12/26 1:51
Author: L1nf3ng
"""

import asyncio
from crawler.models import Executor

async def unit_task(url):
    cl = Executor(url)
    # phase 1, request the blog
    blog = await cl.get_blog()
    if blog is None:
        print('the target {} currently not visited!'.format(url))
    print("---------- the posts from {} -----------".format(url.upper()))
    # phase2, analyse the response
    cl.parse_blog(blog)
    # to_show = {'Origin': url.url, 'Articles': cl.posts, 'Len': len(cl.posts)}
    # temp.append(to_show)
