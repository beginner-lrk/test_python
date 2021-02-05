#! /usr/bin/python
# -*- coding: UTF-8 -*-
def power(x):
    return x * x


print(power(5))


def index(x, n):
    s = 1
    while n >= 1:
        s = s * x
        n = n - 1
    return s


print(index(2, 3))


# 如果实际遇到修改power(x)为power(x, n)要兼容老程序，此时可以增加一个默认参数
def index1(x, n=2):
    s = 1
    while n >= 1:
        s = s * x
        n = n - 1
    return s


print(index1(4))

def enroll(name,gender,age=6,city='杭州'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)
print(enroll('刘','lsd1'))

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))