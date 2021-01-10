# coding = utf-8

# -*- coding: utf-8 -*-
from selenium import webdriver  #导入webdriver 模块

import time

browser = webdriver.Firefox() #调用Firefox()方法打开火狐浏览器
browser.get("http://www.hao123.com") #在浏览器中打开hao123首页

time.sleep(1)

browser.maximize_window() #浏览器最大化

browser.quit() #关闭浏览器
