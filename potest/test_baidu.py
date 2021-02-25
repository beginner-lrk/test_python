#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/2/25 16:44
from selenium import webdriver
from baidu_page import Baidu_page
import unittest
from time import sleep
from parameterized import parameterized
def get_data():
    return [("测试","测试_百度搜索"),("selenium","测试_百度搜索")]

class TestBaidu(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://www.baidu.com"
    def tearDown(self):
        self.driver.quit()
    @parameterized.expand(get_data())
    def test_baidu_search_case1(self,port,expect):
        page =Baidu_page(self.driver)
        page.open(self.url)
        page.search_input(port)
        page.search_button()
        sleep(3)
        self.assertEqual(page.get_title(),expect)