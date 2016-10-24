# -*- conding:utf-8 -*-
import re,urllib.request,pymssql
from sql_active import *
#目的网址
bookurl="http://www.quanshu.net/book/9/9055/"
#获取章节Url,章节名
def getlist():
    html=urllib.request.urlopen(bookurl).read()
    html=html.decode("gb2312")
    reg=re.compile(r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>')
    urls=re.findall(reg,html)
    return urls

#获取章节内容
def getcontent(contenturl):
    html = urllib.request.urlopen(contenturl).read()
    html =html.decode("gbk")
    reg=re.compile(r'style5\(\);</script>(.*?)<script type')
    content=re.findall(reg,html)[0]
    return content

# 执行查询语句，插入语句
def adddata(title,content):
    active = "insert into books values('%s','%s')"%(title,content)
    ms.ExecNonQuery(active) #调用test123.py模块中的MSSQL类的ExecNonQuery 方法

for i in getlist():
    print("正在爬取%s"%i[1])
    title=i[1]
    content=getcontent(bookurl + i[0])
    print ("正在插入数据库%s"%i[1])
    adddata(title,content)