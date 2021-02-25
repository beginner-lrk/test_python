#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/2/25 15:31
'''
把共同操作提取封装到父类中，子类直接调用父类的方法，避免代码冗余
1. 对象库层-基类，把定位元素的方法定义在基类中
2. 操作层-基类，把对元素执行输入操作的方法定义在基类中
'''
import time
class BasePage():
    """
    基础page层，封装常用的一些方法
    """
    #driver = webdriver.Chrome()
    def __init__(self,driver):
        self.driver = driver
        self.url = None
    #打开页面
    def open(self,url):
        if url is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)
    #id定位
    def by_id(self,id_):
        return self.driver.find_element_by_id(id_)

    #name定位
    def by_name(self, name):
        return self.driver.find_element_by_name(name)

    # class 定位
    def by_class(self, class_name):
        return self.driver.find_element_by_class_name(class_name)

    # XPath 定位
    def by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    # CSS 定位
    def by_css(self, css):
        return self.driver.find_element_by_css_selector(css)

    # 获取 title
    def get_title(self):
        return self.driver.title

    # 获取页面 text，仅使用 XPath 定位
    def get_text(self, xpath):
        return self.by_xpath(xpath).text

    # 执行 JavaScript 脚本
    def js(self, script):
        self.driver.execute_script(script)