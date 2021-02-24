#导包
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
'''
显示等待：在抓取瞬间的提示信息有用
1. 导包 等待类 --> from selenium.webdriver.support.wait import WebDriverWait
2. WebDriverWait(driver, timeout, poll_frequency=0.5)
    1). driver：浏览器驱动对象
    2). timeout：超时的时长，单位：秒
    3). poll_frequency：检测间隔时间，默认为0.5秒
3. 调用方法 until(method)：直到...时
    1). method：函数名称，该函数用来实现对元素的定位
    2). 一般使用匿名函数来实现：lambda x: x.find_element_by_id("userA")
        x: 中x为driver,它是WebDriverWait类将传入的driver值赋值给self._driver,until方法调用了self._driver
4. element = WebDriverWait(driver, 10, 1).until(lambda x: x.find_element_by_id("userA")
'''
#实例化WebDriverWait()
WebDriverWait(driver,timeout=10,poll_frequency=0.1).until(lambda x:x.find_element_by_id("#user")).send_keys("admin")
#注意上面的后半段我们敲代码发现pycharm不会自动显示完整函数，因为前面的还没有执行。比如username还不是元素，只有代码运行起来才是元素，可参考如下
# username = WebDriverWait(driver,timeout=10,poll_frequency=0.1).until(lambda x:x.find_element_by_id("#user"))
# username.send_keys("admin")

'''
显示等待针对单个元素
隐式等待针对全局
隐式等待：
    方法：driver.implicitly_wait(timeout)
    (timeout：为等待最大时长，单位：秒)
'''

