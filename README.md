# SecurityDaily
一款用于搜集安全社区各种资讯（博客、公告、情报）的工具，本项目是原BlogSpider项目的提取版，将更加关注信息搜集的功能。

任务配置页面：

![](https://i.loli.net/2021/01/04/fAnUC4OYGqz35tI.png)

结果展示页面:

![](https://i.loli.net/2021/01/04/mOuhBFxRvHy4czX.png)

## 知识早餐计划

**就像身体需要吃早餐，头脑也需要补充知识**

每个早晨，打开工具，让它帮你获取先知、安全客、freebuf、嘶吼等安全社区的资讯，进步源于不断学习。

## 特性

* 爬取框架更加完善，任务结构化，代码更清晰
* 以xpath表达式作为爬虫的规则库
* 以web形式向用户提供服务、结果展示
* 采用协程机制，加快爬取效率
* 支持MySQL、SQLite两种数据库

## 安装

### 1.下载源码

`git clone https://github.com/L1nf3ng/SecurityDaily.git -b main`

### 2.安装依赖

`cd SecurityDaily && python -m pip install -r requirements.txt`

### 3.配置数据库

本项目支持两种数据库：

***

如果使用的是MySQL数据库，将项目根目录下的`mysql.sql`文件拷入某个系统目录（例如:`/home/`），然后进入MySQL执行脚本：

`> source /home/mysql.sql`

执行完会新建一个名为`SecurityDaily`的数据库，对某个mysql用户授予该数据库的全部权力：

`> grant all on SecurityDaily.* to 'your_mysql_account'@'%'; flush privileges;`

切换到项目`dashboard`目录下的`config.py`文件，配置对应的MySQL连接参数。

***

如果使用的是SQLite数据库（本地数据库），则在项目根目录下创建名为`SecurityDaily.db`的数据库，进入该数据库后，执行：

`>.read sqlite3.sql`

***

数据库通过`config.py`文件`DATABASE_TYPE`参数切换。

### 4.运行项目

回到项目根目录，运行：

```bash
# 如果是linux
export FLASK_APP=dashboard
# 如果是CMD
set FLASK_APP=dashboard
# 如果是PowerShell
$env:FLASK_APP=dashboard

python -m flask run
```

## Q&A

1. 为什么记录的是博客链接而非网页本身？
>答： 为了节省存储空间，一般这些资讯网站很少删除旧文章，既然联网就能访问，何必下载网页了。不过后续会开发一键下载功能，方便对中意的文章本地备份。
