'''
Python 中有6大数据类型：
1、number 数字
2、string 字符串
3、list 列表
4、tuple 元组
5、sets 集合
6、dictionary 字典
'''
#一、数字
a = 1
b = 3.14
c = True
print(type(a))
print(type(b))
print(type(c))
print((3+1)) #加法运算，输出结果为4
print((8.4-3)) #减法运算，输出结果为5.4
print(15/4) #除法运算，输出结果为3.75
print(15//4) #整除运算，输出结果为3
print(15%4) #取余运算，输出结果为3
print(2*3) #乘法运算，输出结果为6
print(2**3) #乘方运算，输出结果为8

#二、字符类型
'''
字符串就是在单引号、双引号和三引号之间的文字。
1、单引号示例：print(' welcome to hangzhou '),其中所有的空格和制表符都照原样保留。
2、当引号里面包含单引号时，则该引号需要使用双引号，例如：print("what's your name?")。
3、三引号可以指多行的字符串，也可以在三引号中自由使用单引号和双引号，如下所示。
'''
print('''Mike:Hi,How are you?
LiMing:Fine,Thank you!and you?
Mike:I'm fine, too!''')