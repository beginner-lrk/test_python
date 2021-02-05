#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/2/2 14:33
# range(start, end[,step]) start 表示起始位置，end 表示结束位置，step 表示每次循环的步长
"""for s in "hello":
    print(s)
fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print(fruit)
for i in range(1, 10, 2):
    print(i)"""
#元组
tup1 = ( 'a','b','3','4')
tup2 = (1,2,3)
print(tup1[0])
print(tup2[0:2])
tup3 = tup1 + tup2
print(tup3)
tup4 =("Hi!")
print(tup4 * 3)
#字典
dicts = {"username":"zhangsan" , 'password':123456}
print(dicts.keys())
print(dicts.values())
dicts["age"] = 22
print(dicts["age"])
#循环打印字段keyhe value
for k ,v in dicts.items():
    print("dicts keys is %r" %k)
    print("dicts values is %r" %v)