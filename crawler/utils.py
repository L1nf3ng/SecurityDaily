# -*- encoding:utf-8 -*-

"""
Function: 与任务有关的基本类
Create Time: 2020/12/26 1:51
Author: L1nf3ng
"""

import asyncio
import json
import broadscope_bailian

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


async def askAI(words,content):
    appid, accesskey, secret, agentkey =await getAIcredentials("../credentials/appkeys.txt")
    client = broadscope_bailian.AccessTokenClient(access_key_id=accesskey, access_key_secret=secret,
                                                  agent_key=agentkey)
    token = client.get_token()
    content_templates = "你是一名专业的文章内容摘要专家，请根据我提供的文章内容生成摘要。字数不超过{}。文章内容：{}".format(words, content)
    #查询内容
    messages = [{"role":"user","content":content_templates}]

    resp = broadscope_bailian.Completions(token=token).create(
        app_id=appid,
        messages=messages,
        # 按message方式返回结果
        result_format="message",
        # 超时设置, 单位秒
        timeout=30
    )
    #请求失败，打印原因，后续改成log
    if not resp.get("Success"):
        print('failed to create completion, request_id: %s, code: %s, message: %s' % (
            resp.get("RequestId"), resp.get("Code"), resp.get("Message")))
        return
    #请求成功，读取内容
    content = resp.get("Data", {}).get("Choices", [])[0].get("Message", {}).get("Content")
    print("request_id: %s, content: %s\n" % (resp.get("RequestId"), content))


## test api flow
# if __name__ == "__main__":
#     article_content = """砒霜，这一在古装电视剧中频繁出现，令人闻风丧胆的剧毒之物，在现代医学的巧妙运用下，竟然成为挽救生命的良药，近日，武汉市普仁医院血液内科团队便成功运用砒霜（三氧化二砷）联合维A酸，成功让一名早期急性早幼粒细胞白血病患者重获新生。
#
# 56岁的汪女士（化姓）自今年1月份起便饱受头晕、乏力的困扰，汪女士担心可能是过往的卵巢癌又复发了。1月11日，她来到武汉市普仁医院就诊。经过门诊检查后医生发现，汪女士的白细胞计数明显偏低，仅为1.67(10^9/L)，远低于正常值3.5(10^9/L)，建议她到血液内科就诊。
#
# 常伟主任正在查房
#
# 血液内科医生反复与汪女士进行沟通，耐心解释病情，最终说服她接受了骨髓穿刺检查。检查结果显示，汪女士患上了早期急性早幼粒细胞白血病，这一恶性血液疾病需要迅速而有效地治疗。武汉市普仁医院血液内科主任常伟表示，急性早幼粒细胞白血病患者被发现时，疾病往往是最严重的时候，该病早期死亡率高达50%，多死于颅内出血、重症感染、弥散性血管内凝血（DIC）、恶性贫血等。
#
# 为了尽快遏制汪女士的病痛，常伟主任带领团队迅速为汪女士制定了一套独特的治疗方案——利用三氧化二砷联合维A酸进行治疗。“三氧化二砷，也就是咱们俗称的砒霜，有剧毒，砒霜这种东西用不好就是剧烈毒药，用得好反而能成为治病救人的良药。研究发现小剂量砒霜可以干扰巯基酶活性，调控癌相关基因的表达以及阻碍细胞周期的进程的途径，发挥其抗癌的生物活性。”血液内科主任常伟解释道。
#
# 在血液内科医护团队的精心治疗和护理下，经过维A酸和三氧化二砷的治疗后，2月28日，记者了解到，汪女士的病情得到了显著的改善，头晕、乏力的症状消失无踪，白细胞计数也逐渐恢复正常。“患者目前已经脱离生命危险，现在即将进行下一步的化疗及巩固治疗。”常伟主任表示。
#
# 武汉市普仁医院血液内科主任常伟表示，任何药物都有其两面性，关键在于如何科学、合理地运用它们，为患者带来最大的益处。"""
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(askAI(200, article_content))