import unittest
#新建测试类
version = 30
class Test_02(unittest.TestCase):
    @unittest.skip("test01方法未实现")
    #新建村屙屎方法1
    def test01(self):
        print("01方法实现")
    # 新建村屙屎方法2

    @unittest.skipIf(version > 25,"版本太高跳过用例")
    def test02(self):
        print("02方法实现")
