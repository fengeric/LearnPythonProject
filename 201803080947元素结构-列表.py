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

