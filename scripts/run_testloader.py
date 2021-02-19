#运行common目录下的test_unittest,test_unittest1,test_unittest2三个文件下所有的套件
#一般工作都用下面的办法执行
#导包
import unittest
#调用方法
#site=unittest.TestLoader().discover("../common")
#扩展 执行指定文件目录下的所有套件 方法
site = unittest.TestLoader().discover("../common",pattern="test_canshu*.py")
#扩展  defaultTestLoader = TestLoader()
#site = unittest.defaultTestLoader.discover("../common",pattern="tpshop*.py")
#执行 套件 方法 TexttestRunner
unittest.TextTestRunner().run(site)
#运行结果中 . 符号代表执行通过     F代表失败
