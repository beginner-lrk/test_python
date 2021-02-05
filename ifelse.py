#! /usr/bin/python
# -*- coding: UTF-8 -*-
age = 13
if age >= 30:
    print('你的年龄是', age)
elif 10 < age < 15:
    print("未成年")
else:
    print('青少年')
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x = 0
if x:
    print('True')

birth = int(input('请输入你的生日'))
if birth < 2000:
    print('00前')
else:
    print('00后')

height = int(input('请输入你的身高'))
weight = int(input('请输入你的体重'))
BMI = height / (weight ** 2)
if BMI < 18.5:
    print('过轻')
elif 18.5 <= BMI < 25:
    print('正常')
elif 25 <= BMI < 28:
    print('过重')
elif 28 <= BMI < 32:
    print('肥胖')
else:
    print('严重肥胖')
