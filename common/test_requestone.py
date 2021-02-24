#! /usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2021/2/22 9:39
import requests
import unittest
import json
#不要开启fiddler或其他代理服务，否则会导致请求失败
# 请求url
url_crmhd = "https://crmhd.linker.cc/crm/merchant/vip/getviplist"
# 请求头
headers_crmhd = {"Accept":"application/json, text/plain, */*",
                "Accept-Encoding":"gzip, deflate, br",
                 "Accept-Language":"zh-CN,zh;q=0.9",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
                "PCHT":"212e89142f657883d30267b50c547b6e",
                 "Connection":"close"}
# 查询字符串
param_crmhd = {"pageIndex":"1",
                "pageSize":"20"}
try:
    res = requests.get(url_crmhd, headers=headers_crmhd, params=param_crmhd).status_code
except AssertionError:
    raise
# 获取响应信息头
print("响应状态码：", res)
url_crm = "https://crmhd.linker.cc/crm/shop/goods/list"
# 查询字符串
param_crm = {"key":"","pageIndex":1,"pageSize":20,"status":"","group":[],"goodsType":"","sort":"","sortType":1}
res_po = requests.post(url_crm,data=json.dumps(param_crm),headers=headers_crmhd).status_code
print("响应状态码：",res_po)

class Testvip(unittest.TestCase):
    def test_getvip(self):
        self.assertEqual(res, 200)
    def test_poshop(self):
        self.assertEqual(res_po,200)

if __name__ == '__main__' :
    #实例化对象，对象名为自定义
    site=unittest.TestSuite()
    #调用测试方法
    site.addTest(unittest.makeSuite(Testvip))
    #Test执行测试套件
    runner=unittest.TextTestRunner()
    runner.run(site)
