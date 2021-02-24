#导包
import unittest
import time
from selenium import webdriver
#创建浏览器驱动对象
#driver = webdriber.Firefox()
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
#设置浏览器固定大小
driver.set_window_size(300,200)
#隐式等待
driver.implicitly_wait(30)
#最大化浏览器
driver.maximize_window()
#打开url
driver.get('http://www.baidu.com')
#静默2秒
time.sleep(5)
#设置cookie
driver.add_cookie({"name":"BDUSS","value":"200QUl4TU4zMXlBMjFDUG5QWnZBLU1vc09BaHhYQzNkOEs5MGlyWFlnZ1dGMU5nSVFBQUFBJCQAAAAAAAAAAAEAAAB78wMpyfHLtbK7ysfW7QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABaKK2AWiitgM"})
time.sleep(2)
cookie = driver.get_cookie("BDUSS")
print(cookie)
time.sleep(2)
driver.refresh()
driver.close()
