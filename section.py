#! /usr/bin/python
# -*- coding: UTF-8 -*-
# append() 方法用于在列表末尾添加新的对象
L = ['Bob', 'Tom', 'Liu', 'zhao', 'qian']
r = []
n = 5
for i in range(n):
    r.append(L[i])
print(r)

# 切片功能 L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素
print(L[0:3])
# 如果第一个索引是0可以忽略
print(L[:3])
# 从索引1开始，到索引3为止，不包括索引3
print(L[1:3])
# 从倒数开始切片
print(L[-1:])
print(L[-2:-1])
