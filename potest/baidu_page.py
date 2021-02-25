#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/2/25 10:57
#原则是将所有会用到的元素封装成方法
from base_baidu import BasePage

#封装更多的方法到BasePage类中
class Baidu_page(BasePage):
    def search_input(self,search_key):
        self.by_id("kw").send_keys(search_key)
    def search_button(self):
        self.by_id("su").click()
