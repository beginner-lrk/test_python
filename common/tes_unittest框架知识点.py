'''总结：参考test_unittest文件'''
'''
核心要素
1. TestCase:测试用例
2. TestSuite:测试套件，多个测试用例集合在一起
3. TestRunner：执行测试用例和测试套件
4. TestLoader：加载TestCase到TestSuite中，并把测试用例封装成测试套件；使用unittest.TestLoader，通过该类下面的discover()方法自动搜索指定目录下指定开头的.py文件
，并将查找到的测试用例组装到测试套件
5. Fixture：初始化测试环境或销毁就是一个Fixture
'''
'''
Testcase定义：
    1. 导包：import unittest
    2. 定义测试类：新建测试类必须继承unittest.TestCase
    3. 定义测试方法：测试方法名称命名必须以test开头
Testcase使用：
    方式一：
        使用pycharm在代码上点击鼠标右键，选择使用UnitTest运行
    方式二：
        调用 unittest.main() 来运行
'''
'''
TestSuite使用：
1. 实例化： suite = unittest.TestSuite()
(suite：为TestSuite实例化的名称)
2. 添加用例：suite.addTest(ClassName("MethodName"))        这个不推荐，后面还有更好的
(ClassName：为类名；MethodName：为方法名)
3. 添加扩展：suite.addTest(unittest.makeSuite(ClassName))  这个不推荐，后面还有更好的
(搜索指定ClassName内test开头的方法并添加到测试套件中)
'''
'''
TestRunner的使用：
1. 导包
2. 实例化： runner = unittest.TextTestRunner()
3. 执行：   runner.run(suite) # suite：为测试套件名称
'''
'''
TestLoader：
1.导包
2.调用Testload()
  写法1：site = unittest.TestLoader().discover("指定文件的文件目录","指定字母开头的")
  写法2：site = unittest.defaultTestLoader.discover("指定文件的文件目录","指定字母开头的")
'''
'''
TestLoader和TestSuite区别：
 共同点都是测试套件
 不同点实现方法不同
 TestSuite：需要手动添加测试用例（可以添加测试类，也可以添加测试类中某个测试方法）
 TestLoader：搜索指定目录下指定开头.py文件，并添加测试类中的所有的测试方法，不能指定添加测试方
法
'''
'''
Fixture:
主要用到类和方法，
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
'''

