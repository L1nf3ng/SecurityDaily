# SecurityDaily
一款用于搜集安全社区各种资讯（博客、公告、情报）的工具，由原BlogSpider项目迁移而来，新版本将按主题搜罗信息，将结果限定在固定的几个技术领域内。

## 功能介绍

任务配置页面：

![](https://i.loli.net/2021/01/04/fAnUC4OYGqz35tI.png)

结果展示页面:

![](https://i.loli.net/2021/01/04/mOuhBFxRvHy4czX.png)

## 知识早餐计划

**就像身体需要吃早餐，头脑也需要补充知识**

每个早晨，打开工具，让它帮你获取先知、安全客、freebuf、嘶吼等安全社区的资讯，进步源于不断学习。

## 特性

* 以xpath表达式作为爬虫的规则库
* 以web形式向用户提供服务、结果展示
* 采用协程机制，加快爬取效率
* 支持MySQL、SQLite两种数据库

即将开发：
* 支持设置定时任务保证固定周期自动爬取数据
* 支持AI能力对文章内容快速总结并展示

## 安装

1.下载源码

`git clone https://github.com/L1nf3ng/SecurityDaily.git -b main`

2.安装依赖

`cd SecurityDaily && python -m pip install -r requirements.txt`

3.配置数据库

本项目支持两种数据库：

***

如果使用的是MySQL数据库，将项目根目录下的`mysql.sql`文件拷入某个系统目录（例如:`/home/`），然后进入MySQL执行脚本：

```sql
source /home/mysql.sql
```

执行完会新建一个名为`SecurityDaily`的数据库，对某个mysql用户授予该数据库的全部权力：

```sql
create user 'your_account'@'host' identified by 'your_password';
grant all privileges on SecurityDaily.* to 'your_account'@'host';
flush privileges;
```

切换到项目`dashboard`目录下的`config.py`文件，配置对应的MySQL连接参数。

***

如果使用的是SQLite数据库（本地数据库），则在项目根目录下创建名为`SecurityDaily.db`的数据库，进入该数据库后，执行：

`>.read sqlite3.sql`

***

数据库通过`config.py`文件`DATABASE_TYPE`参数切换。

4.运行项目

启动方式一：python模块启动。回到项目根目录，运行：

```bash
# 如果是linux
export FLASK_APP=dashboard
# 如果是CMD
set FLASK_APP=dashboard
# 如果是PowerShell
$env:FLASK_APP=dashboard

python -m flask run
```

启动方式二：main文件启动。

```bash
python dashboard/views.py
```

## MileStones
**V2.0**

将开发新的AI总结功能，将获取到的网页文本类容做简要概括并展示，提高阅读效率。本功能将率先运用在htrHunter模块内。

**V2.1**

前端页面全面升级，更加美观大气。