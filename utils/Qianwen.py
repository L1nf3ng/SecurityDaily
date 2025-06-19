# -*- encoding:utf-8 -*-

"""
Function: 与任务有关的基本类
Create Time: 2020/12/26 1:51
Author: L1nf3ng
"""

import asyncio
import json
# import broadscope_bailian

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


async def getAIcredentials(filename):
    with open(filename) as file:
        words = file.read()
    contents = json.loads(words)
    return contents["AppId"], contents["AccessKey"], contents["AKsecret"], contents["AgentKey"]



# async def askAI(words,content):
#     appid, accesskey, secret, agentkey =await getAIcredentials("../credentials/appkeys.txt")
#     client = broadscope_bailian.AccessTokenClient(access_key_id=accesskey, access_key_secret=secret,
#                                                   agent_key=agentkey)
#     token = client.get_token()
#     content_templates = "你是一名专业的文章内容摘要专家，请根据我提供的文章内容生成摘要。字数不超过{}。文章内容：{}".format(words, content)
#     #查询内容
#     messages = [{"role":"user","content":content_templates}]
#
#     resp = broadscope_bailian.Completions(token=token).create(
#         app_id=appid,
#         messages=messages,
#         # 按message方式返回结果
#         result_format="message",
#         # 超时设置, 单位秒
#         timeout=30
#     )
#     #请求失败，打印原因，后续改成log
#     if not resp.get("Success"):
#         print('failed to create completion, request_id: %s, code: %s, message: %s' % (
#             resp.get("RequestId"), resp.get("Code"), resp.get("Message")))
#         return
#     #请求成功，读取内容
#     content = resp.get("Data", {}).get("Choices", [])[0].get("Message", {}).get("Content")
#     print("request_id: %s, content: %s\n" % (resp.get("RequestId"), content))
