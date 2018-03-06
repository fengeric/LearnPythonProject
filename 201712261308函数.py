# --------------------------------
def say_hello():
    # 该块属 于这一函数
    print(' hello world')


# 函数结束
say_hello()  # 调用 函数


# --------------------------------
def print_max(a, b):
    if a > b:
        print(a, ' is maximum')
    elif a == b:
        print(a, ' is equal to', b)
    else:
        print(b, ' is maximum')


# 直接传递字面值
print_max(3, 4)

x = 5
y = 7
# 以参数的形 式传递变量
print_max(x, y)


# ------------默认参数值--------------------
# 对于一些函数来说， 你可能为 希望使一些参数可选并使用 默认的值
# 以避免用 户 不想为 他们提供值的情况。 默认参数值可以有效帮 助解决这一情况。 你可以通过在函数定义时附加一个
# 赋值运算符（ = ） 来为 参数指定默认参数值。
def say(message, times=1):
    print(message * times)


say('Hello')  # Hello
say('World', 5)  # WorldWorldWorldWorldWorld


# 注意
# 只有那些位于参数列表末尾的参数才 能被赋予默认参数值， 意即在函数的参数列 表中 拥
# 有默认参数值的参数不能位于没有默认参数值的参数之前。
# 这是因 为 值是按参数所处的位置依次分配的。 举例 来说， def func( a, b=5) 是有效的，但 def func( a=5, b) 是无效的。
# ------------关键字参数--------------------
def func(a, b=5, c=10):
    print(' a is', a, ' and b is', b, ' and c is', c)


func(3, 7)  # a is 3 and b is 7 and c is 10
func(25, c=24)  # a is 25 and b is 5 and c is 24
func(c=50, a=100)  # a is 100 and b is 5 and c is 50


# ------------可变参数--------------------
def total(a=5, *numbers, **phonebook):
    print(' a', a)
    # 遍历 元组中 的所有项目
    for single_item in numbers:
        print(' single_item', single_item)

    # 遍历 字典中 的所有项目
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))


# a 10
# single_item 1
# single_item 2
# single_item 3
# Inge 1560
# John 2231
# Jack 1123
# ------------文档字符串--------------------
def print_max(x, y):
    ''' Prints the maximum of two numbers. 打印两 个数值中 的最大数。
        The two values must be integers. 这两 个数都应 该是整数'''
    x = int(x)
    y = int(y)
    if x > y:
        print(x, ' is maximum')
    else:
        print(y, ' is maximum')


print_max(3, 5)
print(print_max.__doc__)
