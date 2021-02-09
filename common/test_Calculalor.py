#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/2/9 9:10
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
    assert result == 70, '乘法运算失败！'


def test_div():
    fd = Calculalor(9, 2)
    result = fd.div()
    assert result == 4.5, '触发运算失败'


if __name__ == '__main__':
    test_add()
    test_rid()
    test_sub()
    test_div()
