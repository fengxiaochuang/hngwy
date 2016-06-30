# -*- coding: utf-8 -*-

import os

import subprocess

# os.system("'C:/Program Files (x86)/Pandoc/pandoc.exe' -s D:/phpstudy/www/doc.html -o test65.docx")
# subprocess.call (["C:/Program Files (x86)/Pandoc/pandoc.exe", "-s", "D:/phpstudy/www/doc.html", "-o", u"我这个是真的哦也.docx".encode('gbk')],shell=True)

# os.mkdir(u"测试".encode("gbk"))
os.chdir(u"测试".encode("gbk"))
subprocess.call (["C:/Program Files (x86)/Pandoc/pandoc.exe", "-s", "D:/phpstudy/www/doc.html", "-o", u"我这个是真的哦也.docx".encode('gbk')],shell=True)
print os.getcwd()
# tmp = os.popen('pandoc -s D:/phpstudy/www/doc.html -o test65.docx').readlines()
# print tmp
