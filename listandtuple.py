#! /usr/bin/python
# -*- coding: UTF-8 -*-
# 变量classmates就是一个list,x=[ ]
print(1)
classmates = ['tom', 'Bob', '流川']
print(classmates)
print(len(classmates))
# 用索引来访问list中每一个位置的元素，记得索引是从0开始的,最后一个元素的索引是len(classmates) - 1。
print(classmates[0], classmates[1], classmates[len(classmates) - 1])
# 取最后一个元素,倒数第二个，倒数第三个
print(classmates[-1], classmates[-2], classmates[-3])
# 追加元素到末尾
classmates.append('Alan')
print(classmates[-1])
# 插入元素到指定位子
classmates.insert(1, '江河')
print(classmates)
# 删除末尾的元素
classmates.pop()
print(classmates)
# 删除指定的元素
classmates.pop(2)
print(classmates)
# 把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = '山海'
print(classmates)
# 二维数组
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s[2][1])
# tuple和list非常类似，但是tuple一旦初始化就不能修改,没有append()，insert()可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素.
# 因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
# tuple和list.一个是s=(),一个是s=[]
t = (1, 2)
print(t[1])
# 只有1个元素的tuple定义时必须加一个逗号,否则，u=(3)会优先判定数学意义上的括号
u = (3,)
print(u)
# 下一行中为tuple中存在一个list,a,b不可变，A,B是可变的。tuple所谓的“不变”是说，tuple的每个元素，指向永远不变
x = ('a', 'b', ['A', 'B'])
x[2][1] = 'D'
print(x)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[-1][-1])
