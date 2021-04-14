# -*-coding: utf-8-*-
# @Time    : 2021/1/10 14:48
# @Auther  : zhaoyuxiao
# @File    : 1.5 class.py
# @Software: PyCharm

# 创建一个类
class Hello:

    # 构造方法
    def __init__(self, name):
        self._name = name

    # 定义一个方法
    def sayHello(self):
        print("Hello {0}".format(self._name))


#继承类
class Hi(Hello):
    #创建构造方法
    def __init__(self, name):
        #创建副类的构造方法
        Hello.__init__(self, name)

    #继承定义方法
    def sayHi(self):
        print ("Hi {0}".format(self._name))

# 创建一个Hello的实例
run = Hello("zhaoyuxiao")
run.sayHello()

# 创建一个Hi的实例
run2 = Hi("zhaoyuxiao2")
run2.sayHi()
