#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/3/1 14:45
import os
#返回当前文件所有文件夹路径
print(os.getcwd())
#返回path的绝对路径
print(os.path.abspath("ostest.py"))
#如果path是一个存在的路径，返回True，否则（otherwise） 返回 False
print(os.path.exists("../logs"))
log_dir = '../logs'
log_file='../logs/log.txt'
#判断路径是否存在,，不存在则创建
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
#判断文件是否存在,，不存在则创建
if not os.path.isfile(log_file):
    with open("abc.txt", mode="w", encoding="utf-8") as f:  # 写文件,当文件不存在时,就直接创建此文件
        pass

'''
关于open 模式：
w     以写方式打开，
a     以追加模式打开 (从 EOF 开始, 必要时创建新文件)
r     以读写模式打开
w+     以读写模式打开 (参见 w )
a+     以读写模式打开 (参见 a )
rb     以二进制读模式打开
wb     以二进制写模式打开 (参见 w )
ab     以二进制追加模式打开 (参见 a )
rb+    以二进制读写模式打开 (参见 r+ )
wb+    以二进制读写模式打开 (参见 w+ )
ab+    以二进制读写模式打开 (参见 a+ )
'''


