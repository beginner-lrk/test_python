#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/2/9 13:16
import unittest
from test_unitsample import Calculalor

class TestCalculalor(unittest.TestCase):

    #测试用例前置动作
    def setUp(self):
        print("测试开始")

    def tearDown(self):
        print("测试结束")

    def test_add(self):
        c=Calculalor(5,6)
        result = c.add()
        self.assertEqual(result,11)

    def test_sub(self):
        d=Calculalor(5,2)
        result=d.sub()
        self.assertEqual(result,3)

    def test_rid(self):
        e=Calculalor(10,2)
        result=e.rid()
        self.assertEqual(result,20)

    def test_div(self):
        f=Calculalor(10,4)
        result=f.div()
        self.assertEqual(result,2.5)

if __name__ == '__main__':
    #创建测试套件
    suit = unittest.TestSuite()
    suit.addTest(TestCalculalor("test_add"))
    suit.addTest(TestCalculalor("test_sub"))
    suit.addTest(TestCalculalor("test"))
    #创建测试运行器
    runner =unittest.TextTestRunner()
    runner.run(suit)
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
    @classmethod   #修饰器修饰类方法
    def setUpClass(cls):
        print("开始执行类")
    @classmethod
    def tearDownClass(cls):
        print("类执行完毕")
    def setUp(self):
        print("执行方法开始")
    def tearDown(self):
        print("执行方法结束")

    def test_add(self):
        c=Calculalor(5,3)
        result=c.add()
        self.assertEqual(result,8)
    def test_sub(self):
        d=Calculalor(7,3)
        dd=d.sub()
        if dd > 1:
            result = True
        else:
            result = False
        self.assertTrue(result)
    def test_mul(self):
        e=Calculalor(4,4)
        result = e.rid()
        self.assertEqual(result,16)
    def test_div(self):
        g=Calculalor(8,4)
        result =g.div()
        self.assertEqual(result,2)
'''
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
'''