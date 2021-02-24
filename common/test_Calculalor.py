#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/2/9 9:10


#传统函数执行测试用例
from test_unitsample import Calculalor


def test_add():
    cd = Calculalor(3, 5)
    result = cd.add()
    assert result == 8, '加法运算失败！'


def test_sub():
    dd = Calculalor(7, 2)
    result = dd.sub()
    assert result == 5, '减法运算失败！'


def test_rid():
    ed = Calculalor(8, 9)
    result = ed.rid()
    assert result == 72, '乘法运算失败！'


def test_div():
    fd = Calculalor(9, 2)
    result = fd.div()
    assert result == 4,'触发运算失败'

if __name__ == '__main__':
    test_add()
    test_rid()
    test_sub()
    test_div()
'''
__name__:为python中内置变量
1.如果当前运行的模块为当前模块，那么__name__的值为：__main__
2.如果当前运行的模块不是主模块(比如这个模块被别的模块引用了)，那么__name__的值为：模块名称(test_Calculalor)
'''