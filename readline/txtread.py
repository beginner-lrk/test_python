#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/3/1 15:44
#导包
import pymysql
import codecs
import csv
#定义数据库链接
def get_conn():
    conn = pymysql.Connect(host="192.1.3.149",
                       port=3306,
                       database="woa_scrm",
                       user="woa",
                       password="Hzlh2020s",
                       autocommit=True
                       )
    return conn
#定义脚本执行，返回元组
def sql_exwcute(oursor,sql,arg):
    oursor.execute(sql,arg)
    return oursor.fetchall()
#
def read_mysql_csv(filename):
    with codecs.open(filename=filename,mode='w',encoding='utf-8') as f:
        write = csv.writer(f,dialect='excel')
        write.writerow(['用户名称','用户账号'])
        conn= get_conn()
        cur= conn.cursor()
        sql = 'SELECT UserCode,UserName from uc_tuserbase'
        users= sql_exwcute(cur,sql,arg=None)
        for user in users:
            print(user)
            write.writerow(user)
read_mysql_csv("./userbase.csv")