#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/2/9 13:16

#导入unittest包
import unittest
from time import sleep

from selenium import webdriver

#定义测试类并继承
class TestShopLogin(unittest.TestCase):
    #定义初始化方法
    def setUp(self):
        self.driver = webdriver.Chrome()
    #打开url
        self.driver.get("http://www.baidu.com")
    #最大化浏览器
        self.driver.maximize_window()
    #隐式等待
        self.driver.implicitly_wait(30)
    #定义tearDown
    def tearDown(self):
        #关闭浏览器驱动
        sleep(3)
        self.driver.quit()
    #定义登录测试并搜索
    def test_login_code_null(self):
        driver= self.driver
        #点击登录链接
        driver.find_element_by_css_selector('[id*=kw]').send_keys("测试")
        driver.find_element_by_css_selector('[id*=kw]').click()
        #随便写的测试记过，如果是提示相当于获取提示内容
        result = driver.find_element_by_css_selector("'[id*=kw]'").text
        #定义预期结果
        expect_result = "验证码不能为空！！"
        try:
        #断言
            self.assertEqual(expect_result,result)
        except AssertionError:
            #截图
            driver.get_screenshot_as_file("../image/error.png")
            #抛出异常
            raise