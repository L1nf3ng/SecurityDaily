# -*- encoding:utf-8 -*-

"""
Function: 与任务有关的基本类
Create Time: 2020/12/26 1:51
Author: L1nf3ng
"""

import asyncio
import json

import os
from openai import OpenAI



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


if __name__ == '__main__':


    try:
        client = OpenAI(
            # 若没有配置环境变量，请用阿里云百炼API Key将下行替换为：api_key="sk-xxx",
            api_key="sk-70c8711e84904a5b8229a4f39911c096",
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        )

        completion = client.chat.completions.create(
            model="qwen-turbo-2025-04-28",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
            messages=[
                {'role': 'system', 'content': r'你是一名网络安全研究员，请根据我提供的文章内容生成摘要。'},
                {'role': 'user', 'content': r'''Description A regular expression denial of service (ReDoS) vulnerability has been identified in the Hugging Face Transformers library's dynamic module utilities. The vulnerability exists in the get_imports() function in dynamic_module_utils.py, which uses a vulnerable regular expression pattern to filter out try/except blocks from Python code. The regex pattern \s*try\s*:.*?except.*?: can be exploited to cause excessive CPU consumption through crafted input strings due to catastrophic backtracking. Technical Details • Affected Component: transformers.dynamic_module_utils.get_imports • Vulnerability Type: Regular Expression Denial of Service (ReDoS) • Attack Vector: Maliciously crafted files containing nested try/except blocks  The proof of concept demonstrates that by providing increasingly long strings with repeated try/except patterns, the execution time grows exponentially, indicating catastrophic backtracking in the underlying regular expression matching.'''}
            ]
        )
        print(completion.choices[0].message.content)
    except Exception as e:
        print(f"错误信息：{e}")
        print("请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code")