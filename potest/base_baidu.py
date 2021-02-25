#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/2/25 15:31

from selenium import webdriver


class BasePage():
    """
    基础page层，封装常用的
    """
    driver = webdriver.Chrome()
    # def __init__(self,driver):
    #     self.driver = driver
    #打开页面
    def open(self,url):
        if url is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)
    #id定位
    def by_name(self,id_):
        return self.driver.find_element_by_id()