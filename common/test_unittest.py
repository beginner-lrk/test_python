#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/2/9 13:16
'''
使用unittest框架测试用例步骤：
1.导包
2.实例化Testsuit对象
3.调用addTest方法添加用例到指定套件中
'''
#导入unittest包
import unittest
#导入要调用的类
from test_unitsample import Calculalor
#定义测试类并继承
class TestCalculalor(unittest.TestCase):
    def test_add(self):
        c=Calculalor(5,3)
        result=c.add()
        self.assertEqual(result,8)
    def test_sub(self):
        d=Calculalor(7,3)
        result=d.sub()
        self.assertEqual(result,4)
    def test_mul(self):
        e=Calculalor(4,4)
        result = e.rid()
        self.assertEqual(result,16)
    def test_div(self):
        g=Calculalor(8,4)
        result =g.div()
        self.assertEqual(result,2)

if __name__ == '__main__' :
    #实例化对象，对象名为自定义
    site=unittest.TestSuite()
    #调用测试方法
    #写法1：类名("方法名") 注意:方法名称使用双引号
    # site.addTest(TestCalculalor("test_add"))
    # site.addTest(TestCalculalor("test_sub"))
    # site.addTest(TestCalculalor("test_mul"))
    # site.addTest(TestCalculalor("test_div"))
    ##写法2
    site.addTest(unittest.makeSuite(TestCalculalor))
    #Test执行测试套件
    runner=unittest.TextTestRunner()
    runner.run(site)