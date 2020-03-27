import hashlib
from flask import json
import os
from setting import BASE_PATH




# 定义一个MD5加密函数,返回值是32位的小写
def md5_code_32_lower(password):
    md5=hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

#定义一个MD5加密函数,返回值是16位的小写
def md5_code_16_lower(password):
    return md5_code_32_lower(password)[:16]


#定义一个密码通过MD5加密后，将32位小写转化为大写
def md5_code_32_upper(password):
    return md5_code_32_lower(password).upper()


#定义一个将字典格式转化为json格式
def json_data(dct):
    json.dumps(dct)
    return json.dumps(dct)

#读取不同接口的URL
def get_url(api_name):
    with open(os.path.join(BASE_PATH,'API_url.txt')) as f:
        datas=f.readlines()
    for api in datas:
        api_f=api.strip("\r\n\t")
        api_c=api_f.split("=")
        if api_name==api_c[0]:
                return api_c[1]




