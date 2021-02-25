#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/2/25 16:44
from selenium import webdriver
from baidu_page import Baidu_page
import unittest
from time import sleep

class TestBaidu(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://www.baidu.com"
    def tearDown(self):
        self.driver.quit()

    def test_baidu_search_case1(self):
        page =Baidu_page(self.driver)
        page.open(self.url)
        page.search_input("测试")
        page.search_button()
        sleep(3)
        self.assertEqual(page.get_title(),"测试_百度搜索")