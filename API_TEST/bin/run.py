import os
import sys
import unittest
import time
from BeautifulReport import BeautifulReport
from setting import CASE_PATH,REPORT_PATH
from lib.send_mail import new_file,send_mail




#查找用例
discover=unittest.defaultTestLoader.discover(CASE_PATH,"test_login.py")

#执行并生成报告
title="接口测试"
time_now=time.strftime("%Y%m%d%H%M%S")
report_name="%s-接口测试报告" %(time_now)

runner=BeautifulReport(discover)
runner.report(description=title,filename=report_name,report_dir=REPORT_PATH)


new_report_mail = new_file(REPORT_PATH)
# log.info(new_report_mail)
send_mail(new_report_mail)
# fp.close()
# pattern=

