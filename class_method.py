#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/2/3 18:59
# 定义add()函数
def add(a, b):
    print(a + b)


# 调用add()函数
add(3, 5)


# 通过return返回结果，变量c接收
def adda(a, b):
    return a + b


c = adda(3, 5)
print(c)


# 设置函数默认值
def addb(a=1, b=2):
    return a + b


c1 = addb()
c2 = addb(3, 5)
print(c1, c2)


# 定义class类
class MyClass(object):
    def say_hello(self, name):
        return "hello," + name


# 调用MyClass类
mc = MyClass()
print(mc.say_hello("Tom"))


# 创建类时常用初始化方法__init__()
class A:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b


# 调用类时需要传入初始化参数
count = A(4, 5)
print(count.add())


# B类继承A类
class B(A):
    def sub(self,a,b):
        return a - b

print(B(3,4).add())
