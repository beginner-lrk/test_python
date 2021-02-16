'''
 断言练习案例：
    输入：正确的账号密码 验证码为空
    断言：提示信息是否为，验证码不能为空！
    要求：如果断言出错，截屏保存
'''
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
#静默2秒
time.sleep(2)
#最大化浏览器
driver.maximize_window()
#打开url
driver.get('http://www.baidu.com')
#静默2秒
time.sleep(10)
#定位登录
#driver.find_element(By.CSS_SELECTOR,'//*[@id="kw"]').clear()
#定位登录常规写法(Ctrl+鼠标左键可以发现是上面那种底层定义过的)
driver.find_element_by_xpath('//*[@id="kw"]').clear()
driver.find_element_by_css_selector('[id*=kw]').send_keys("测试")
driver.find_element_by_css_selector('[value*=百度一下]').click()
text=driver.find_element_by_css_selector('[value*=百度一下]').text
print("按钮的文案是：",text)
size=driver.find_element_by_css_selector('[value*=百度一下]').size
print("按钮的大小是：",size)
att=driver.find_element_by_css_selector('[value*=百度一下]').get_attribute("type")
print("属性值是：",att)
scan=driver.find_element_by_css_selector('[value*=百度一下]').is_displayed()
print("判断属性是否可见：",scan)
#静默2秒
time.sleep(2)
#获取当前页面title
#title=driver.title
#print("当前页面为",title)
#刷新当前页面,这个在获取cookie有用
driver.refresh()
#使用时间戳截图
driver.get_screenshot_as_file("./image/%s.png")
#静默2秒
time.sleep(2)
#执行后退
driver.back()
#静默2秒
time.sleep(2)
driver.find_element_by_css_selector('[class*=odd]').click()
#静默2秒
time.sleep(2)
#获取当前页面url
current=driver.current_url
print("当前页面地址为",current)
#静默2秒
time.sleep(5)
#关闭当前主窗口
driver.close()
#执行前进
#driver.forward()
#静默2秒
time.sleep(2)
#关闭driver程序启动的所有窗口
driver.quit()


'''
#定义测试类并继承
class TestShopLogin(unittest.TestCase):
    #定义初始化方法
    def setUp(self):
        #获取浏览器登录对象
        self.driver =webdriver.
        #最大化浏览器

        #隐式等待

        pass
    #定义tearDown
    def tearDown(self):
        pass
    #定义登录测试方法 验证码为空
    def test_login_code_null(self):

'''