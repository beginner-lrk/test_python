#! /usr/bin/python
# -*- coding: UTF-8 -*-
# for...in循环，依次把list或tuple中的每个元素迭代出来
names = ['abc', 'Bob', 'Lucy']
for na in names:
    print(na)
sum2 = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum2 = sum2 + x
print(sum2)
# 使用range()函数生成从0开始的整数序列，再使用for in 进行0到100的相加
su = 0
for y in range(101):
    su = su + y
print(su)
# while循环
sum1 = 0
n = 100
while n > 0:
    sum1 = sum1 + n
    n = n - 1
print(sum1)

for M in ['Bart','Lisa','Adam']:
    print(M)

#break提前退出循环
a = 1
while a < 10:
    if a > 5:
        break
    a = a + 1
    print(a)
print(a)

#continue
print('输出所有奇数')
b = 0
while b < 10:
    b = b +1
    if b % 2 ==0:
        continue
    print(b)