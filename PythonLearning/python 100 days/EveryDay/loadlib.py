# -*-coding: utf-8-*-
# @Time    : 2021/1/10-15:46
# @Auther  : zhaoyuxiao
# @File    : 1.6.2 loadlib.py
# @Software: PyCharm

# #方法一：直接引用
# import mylib
#
# run = mylib.Hello()
# run.sayHello()

#方法二:详细引用
from mylib import Hello

run = Hello()
run.sayHello()