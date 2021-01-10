# -*-coding:utf-8-*-
def sayHello():
    print("Hello World!")
    # sayHello()
    # 如果缩进表示在方法里面


sayHello()  # 这里直接执行，没有缩进


def max(a, b):
    if a > b:
        return a
    else:
        return b


print(max(1, 2))
