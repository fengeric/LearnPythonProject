# python有四种数据结构
# 列表(列表和元组，感觉使用列表比较好)、字典、元组、集合
# --------------------------------------
# list = [val1, val2, val3, val4]
# dict = {key1: val1, key2: val2}
# tuple = (val1, val2, val3, val4)
# set = {val1, val2, val3, val4}
# --------------------------------------
# 列表 list
weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(weekday[0])

# 插入元素
weekday.insert(0, 'Saturday')
print(weekday)

# 移除元素
weekday.remove('Tuesday')
print(weekday)

del weekday[0]
print(weekday)

# 替换元素
weekday[1] = 'Sunday'
print(weekday)

# 列表索引
print(weekday[:])
print(weekday[1:4])

# 利用sorted排序
num_list = [6, 2, 7, 4, 1, 3, 5]
print(sorted(num_list))  # 排序
print(sorted(num_list, reverse=True))  # 反向排序

# 添加元素
arr = []
for i in range(1, 11):
    arr.append(i)
print(arr)

b = [i for i in range(1, 11)]  # 此方法效率更快
print(b)

# 列表类似生成方法如下
a = [i ** 2 for i in range(1, 10)]  # 输出范围内的数的平方
print(a)

c = [j + 1 for j in range(1, 10)]  # 在取值范围内加1输出
print(c)

k = [n for n in range(1, 10) if n % 2 == 0]  # 取出范围内的偶数
print(k)

z = [letter.lower() for letter in 'ABCDEFGHIJKLMN']
print(z)

# 获取元素索引下标
lett = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for num, letter in enumerate(lett):
    print(letter, 'is', num)
