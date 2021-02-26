#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/2/26 10:41
import pymysql
#step1:创建连接，调用connect函数
conn = pymysql.Connect(host="",
                       port=3306,
                       database="woa_scrm",
                       user="woa",
                       password="Hzlh2020s",
                       autocommit=True
                       )

#step2:创建游标对象，用来给数据库发送sql语句，并执行
cursor = conn.cursor()
#查看数据库是否连接成功
cnn =conn.open
if cnn == True:
    print("数据库连接成功")
else:
    print("数据库连接成功")
#step3:发送sql语句
sql = "SELECT * FROM busi_merchant_saler where ORG_ID=10092;"
#step4:执行sql
cursor.execute(sql)
#step5:获取查询到的数据，默认元组所以要for in 来获取具体数值
salers = cursor.fetchall()
for saler in salers:
    print("CUSTOMER_ID:",saler[0])
    print("PHONE:",saler[7])
'''
默认情况下，新增/修改/删除操作不会提交到数据库
# 方案1:手动提交 conn.commit() 
# 方案2:设置自动提交 创建 conn 时，设置参数 autocommit = True (默认是 False)
'''
#step6:资源释放
cursor.close()
conn.close()
