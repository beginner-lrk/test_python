#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/2/8 16:22
#无测试框架情况下
# 计算机类
class Calculalor:
    # 加减乘除
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def rid(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b