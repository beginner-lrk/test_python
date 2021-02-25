#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/2/25 10:57
#原则是将所有会用到的元素封装成方法
class Baidu_page:
    #初始化驱动
    def __init__(self,driver):
        self.driver= driver
    #封装search_input方法
    def search_input(self,search_key):
        self.driver.find_element_by_id("kw").send_keys(search_key)
    #封装search_button方法
    def search_button(self):
        self.driver.find_element_by_id("su").click()
