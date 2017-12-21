print("hahaha")
#被双引 号包括的字符串 和被单引 号括起的字符串 其工作机制完全相同
#你可以通过使用 三个引 号—— """ 或 ' ' ' 来指定多 行字符串 。 你可以在三引 号之间 自 由 地使用 单引 号与 双引 号。
#--------------------------------------------
#format的用法,Python 中 format 方法所做的事情便是将每个参数值替换至格式所在的位置
name = "feng"
age = 20
print("1{0} was {1} years old when he wrote this book".format(name, age))
print( '2{} was {} years old when he wrote this book'.format(name, age))
print( '3Why is {0} playing with that python?'.format(name))
print( '4Why is {} playing with that python?'.format(name))
#--------------------------------------------
print('a')#和下面一行代码意思一样
print('a',end="\n")
#****
print('a',end="")#打印时不换行
print('b',end="")#打印时不换行
#****
print('a',end=" ")#通过 end 指定以空格结尾
print('b',end=" ")#通过 end 指定以空格结尾
print('c')
#--------------------------------------------
#使用 四个空格来缩进。 这是来自 Python 语言官方的建议
#不使用分号
