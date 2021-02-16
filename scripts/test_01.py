#导包
from time import sleep
from selenium import webdriver
#获取浏览器驱动对象
driver = webdriver.Chrome()
#打开本地Url
Url = r"E:\python\阶段五 web自动化测试\第二章 Selenium-API操作\课堂素材\注册A.html"
driver.get(Url)
#输入admin
driver.find_element_by_css_selector("[id*=userA]").clear()
driver.find_element_by_css_selector("[id*=userA]").send_keys("13156789456")

#输入密码
driver.find_element_by_css_selector("[id*=passwordA]").clear()
driver.find_element_by_css_selector("[id*=userA]").send_keys("123456")
#输入电话
driver.find_element_by_css_selector("#telA").clear()
driver.find_element_by_css_selector("#telA").send_keys("1356497787")
#输入邮箱
driver.find_element_by_css_selector("#emailA").clear()
driver.find_element_by_css_selector("#emailA").send_keys("1234@qq.com")
#暂停2秒
sleep(2)

#修改电话号码--->清空
driver.find_element_by_css_selector("#telA").clear()
driver.find_element_by_css_selector("#telA").send_keys("1356497111")
#暂停2s
sleep(2)
#点击注册按钮
driver.find_element_by_css_selector("button").click()
sleep(2)
driver.quit()
