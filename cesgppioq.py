#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/2/4 20:30
class Animal:
    def heshui(self):
        print('动物正在喝水')

class Cat(Animal):
    def heshui(self):
        print('猫正在喝水')
cat = Cat()
cat.heshui()