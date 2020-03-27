# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/25 17:30
# @Author  : hejun
# @Site    :
# @File    : login_case
# @Software: PyCharm


import unittest
import requests
from lib.utils import json_data,get_url
import ddt,os
from setting import DATA_PATH



@ddt.ddt
class RegisterTest(unittest.TestCase):

    @ddt.file_data(os.path.join(DATA_PATH,'login.yaml'))
    def test_register_01(self,**case):
        self._testMethodDoc = case.get('detail')
        URL=get_url("login")
        method=case.get('method')
        datas=case.get('datas')
        ret=case.get('ret')
        err_code=case.get('err_code')
        err_msg = case.get('err_msg')
        uuid = case.get('uuid')
        msg=case.get('msg')

        if method.lower()=='post':
            r=requests.post(URL,json_data(datas))
            resp=r.json()
            self.assertEqual(ret, resp.get('ret'))                          # 对响应体中ret的状态码进行断言
            self.assertEqual(err_code, resp.get('data').get('err_code'))    # 对响应体中err_code状态码进行断言
            self.assertEqual(err_msg, resp.get('data').get('err_msg'))      # 对响应体中err_msg信息进行断言
            # self.assertIsNotNone(uuid , resp.get('data').get('uuid'))     # 对uuid和msg进行断言
            # self.assertIsNotNone(msg,resp.get('msg'))

        else:
            r=requests.get(URL,datas)
            resp = r.json()
            self.assertEqual(ret, resp.get('ret'))                          # 对响应体中ret的状态码进行断言
            self.assertEqual(err_code, resp.get('data').get('err_code'))    # 对响应体中err_code状态码进行断言
            self.assertEqual(err_msg, resp.get('data').get('err_msg'))      # 对响应体中err_msg信息进行断言
            # self.assertIsNotNone(uuid, resp.get('data').get('uuid'))      # 对uuid和msg进行断言
            # self.assertIsNotNone(msg, resp.get('msg'))
