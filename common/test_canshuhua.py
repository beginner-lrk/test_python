#unittest暂不支持参数化，需要用到插件parameterized:pip install parameterized

#导包
import unittest

from parameterized import parameterized


def ADD(x,y):
    return x+y

def get_data():
    return [(1,2,3),(3,0,3),(2,1,3)]
#定义测试类并继承
class Test01(unittest.TestCase):
    @parameterized.expand(get_data())
    def test_addc(self,x,y,result):
        #调用函数
        except_result = ADD(x,y)
        assert(result,except_result)
#最后使用script下的run_testloader.py执行
