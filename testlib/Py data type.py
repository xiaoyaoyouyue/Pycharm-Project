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
#要使用单引号或者双引号本身，需要借助于转义符（\）
print('what\'s your name?')
#不需要使用转义符进行特别处理的字符串，那么需要指定一个原始字符串，例如加上前缀r或R
print(r"Newlines are indicated by \n")
#字符串的截取
#字符串变量[start_index:end_index+1]
#备注：字符串的截取从start_index开始，到end_index结束，也就是大家常理解的左闭右开，如下所示：
str='Lingyi'
print(str[0]) #输出结果为L
print(str[1:4]) #输出结果为ing
print(str[-1]) #输出结果为i
#字符运算
num=1
string='1'
str=int(string) #string是字符串，不同数据类型之间不能直接进行运算，但是不同数据类型可以相互转换
print(num+str) #注意：“+”号用在字符串中间是连接符，用在数值中间是运算符：int()是括号中的数值或者文本转换成整数数据类型
#四则基础运算如下：
a=1
b=2
c=a+b
print(c)
#因为相加的双方是数值型，此时"+"号是运算符
#相加的双方是字符型数据，此时“+”号是连接符
c='a'+'b'
print(c)


