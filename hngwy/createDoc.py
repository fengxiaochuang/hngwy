# python
# -*- coding: utf-8 -*-
import os
import subprocess

import io

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from hngwy.model.Page import Page
from hngwy.model.Category import Category
from hngwy.util import file as fu

# 1. 按照网址分类创建文件夹

engine = create_engine('mysql+mysqldb://root:root@127.0.0.1:3306/hngwy?charset=utf8')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
db = DBSession()
basepath = os.getcwd()
htmlbasepath = basepath + "/html/"
paperbasepath = basepath + "/paper/"

# 查询分类 并且缓存
category = db.query(Category).all()
# print category
categoryDict = {item.id: {"name": item.name} for item in category}

# 月份列表
mlist = db.execute(
    "SELECT date_format(date,'%Y%m') AS dt, COUNT(date_format(date,'%Y%m')) as c FROM page where date_format(date,'%Y%m') >= 201601 GROUP BY date_format(date,'%Y%m')")

for cate in category:
    if cate.pid == 0:
        pass
    else:
        # print categoryDict[cate.pid] + "/" + categoryDict[cate.id]
        basepath = categoryDict[cate.pid]["name"] + "/" + categoryDict[cate.id]["name"]
        htmlpath = htmlbasepath + basepath
        paperpath = paperbasepath + basepath
        # fu.createPath(htmlpath.encode('gbk'))
        # fu.createPath(paperpath.encode('gbk'))
        tmpdict = categoryDict[cate.id]
        tmpdict["htmlpath"] = htmlpath
        tmpdict["paperpath"] = paperpath
        categoryDict[cate.id] = tmpdict

# 判断
# 2. 生成html的文件
mlist = db.execute(
    "SELECT date_format(date,'%Y%m') AS dt, COUNT(date_format(date,'%Y%m')) as c FROM page where date_format(date,'%Y%m') >= 201601 GROUP BY date_format(date,'%Y%m')")

for d in mlist:
    print(d)
    # 查询所属日期的文章,然后拼接
    page_list = db.execute(
        "select title,content,category from page where date_format(date,'%Y%m')=:dates order by date",
        {'dates': d[0]})
    tmphtml = ""
    # print page_list.rowcount
    for page in page_list:
        tmptitle = page[0]
        tmpcontent = page[1]
        tmpcategory = page[2]
        # print tmptitle
        # print tmpcontent
        # print tmpcategory
        tmphtml += "<h1>" + tmptitle + "</h1>\n" + tmpcontent + "\n<hr>\n"

    tmpfile = str(d[0]) + ".html"
    thisfile = htmlbasepath + tmpfile
    # print thisfile
    # print tmphtml
# print mlist
# a.分类
# b.分月
# 3. 用指令生成doc文档
# 根据html生成对应的doc放置在另外一个文件夹中
    fu.save_file(thisfile, tmphtml.encode("UTF-8"))
    os.chdir(paperbasepath)
    savefile = str(d[0]) + ".doc"
    subprocess.call(["C:/Program Files (x86)/Pandoc/pandoc.exe", "-s", thisfile, "-o", savefile], shell=True)


