
#导包
import unittest
import time
from selenium import webdriver
#创建浏览器驱动对象
#driver = webdriber.Firefox()
from selenium.webdriver import ActionChains
driver =webdriver.Chrome()
#打开url
driver.get('http://www.baidu.com')
#静默2秒
time.sleep(2)
#实例化并获取ActionChains类
action = ActionChains(driver)
#获取用户名
username = driver.find_element_by_css_selector("#userA")
#调用右击方法并执行
action.context_click(username).perform()
#发送用户名并双击执行
username.send_keys("admin")
action.double_click(username).perform()
#移动到注册按钮上
action.move_to_element(driver.find_element_by_css_selector("button")).perform()
#静默2秒
time.sleep(2)
#关闭driver程序启动的所有窗口
driver.quit()
'''
鼠标操作：
1. context_click(element) 右击 --> 模拟鼠标右键点击效果
2. double_click(element) 双击 --> 模拟鼠标双击效果
3. drag_and_drop(source, target) 拖动 --> 模拟鼠标拖动效果
4. move_to_element(element) 悬停 --> 模拟鼠标悬停效果
5. perform() 执行 --> 此方法用来执行以上所有鼠标操作
  步骤：
    1.先导包 from selenium.webdriver import ActionChains
    2.实例化并获取ActionChains类 xx = ActionChains(driver)
    3.元素定位并给到对象 xx = driver.find_element_by_css_selector("#userA")
    4.对象调用方法并执行 action.context_click(xx).perform()
    3和4合并以后：action.context_click(driver.find_element_by_css_selector("userA")).perform()
'''

