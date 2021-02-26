#! /usr/bin/pythpyon
# -*- coding: UTF-8 -*-
# @Time : 2021/2/26 14:53
import traceback

import pymysql
#step1：数据库链接
conn = pymysql.Connect(host="192.1.3.149",
                       port=3306,
                       database="woa_usercenter",
                       user="woa",
                       password="Hzlh2020s",
                          )
#step2:创建游标对象
con = conn.cursor()
#step3:sql语句并发送
try:
    sql1 = "INSERT INTO `uc_tuserbase` VALUES ('fdb06846-5f20-42cd-81f6-4ce280791111', 402, NULL, NULL, 'mbl1830509761', '477255324ffe401128f11a556c6263c8', 'Helloworld', NULL, 3, NULL, 1, NULL, NULL, NULL, NULL, NULL, 1, '', NULL, '2020-04-01 13:43:43', 9, 0, NULL, 'syssteplinkb', '2020-03-17 13:16:59', NULL, NULL, NULL, 1, 0, '10033', NULL, NULL, -1, 0)"
    sql2 = "INSERT INTO `uc_tuserbase` VALUES ( 'Helloworld', NULL, 3, NULL, 1, NULL, NULL, NULL, NULL, NULL, 1, '', NULL, '2020-04-01 13:43:43', 9, 0, NULL, 'syssteplinkb', '2020-03-17 13:16:59', NULL, NULL, NULL, 1, 0, '10033', NULL, NULL, -1, 0)"
    con.execute(sql1)
    con.execute(sql2)
    # 如果上述两条 SQL 语句执行正常,手动提交
    conn.commit()
except Exception as e:
    # traceback.print_exc(file = open('./log.txt', 'sql1'))
    print(e)
    #数据库操作回滚
    conn.rollback()
finally:
    conn.close()
    con.close()