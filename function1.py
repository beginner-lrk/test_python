#! /usr/bin/python
# -*- coding: UTF-8 -*-
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-6.6))
print(abs(-6.6))


# 如果传入不恰当的参数上面定义的会报错，下面优化下只允许传入整数和浮点类型.
# 用到内置函数isinstance(object, classinfo)
# raise 表示触发了异常，后面的不会继续执行
def my_abw(y):
    if not isinstance(y, (int, float)):
        raise TypeError('参数类型错误')
    if y >= 0:
        return y
    else:
        return -y


print(my_abw('A'))


# 定义好的my_abs函数可以在另外一个文件（当前目录）下调用：from function1 import my_abs
# 定义一个空函数，pass表示程序什么都不做,比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来
def nop():
    pass


age = 18
if age >= 20:
    pass
