# python有四种数据结构
# 列表(列表和元组，感觉使用列表比较好)、字典、元组、集合
# --------------------------------------
# list = [val1, val2, val3, val4]
# dict = {key1: val1, key2: val2}
# tuple = (val1, val2, val3, val4)
# set = {val1, val2, val3, val4}
# --------------------------------------
# 字典

ELE = {
    'BIDU': 'Baidu',
    'SINA': 'Sina',
    'YOKU': 'YouKu'
}

# 添加单一元素
ELE['HaHa'] = 'Smile'
print(ELE)

# 添加多个元素
ELE.update({'FB': 'FaceBook', 'TSLA': 'Tesla'})
print(ELE)

# 删除元素
del ELE['YOKU']
print(ELE)

# 索引 需要key来进行索引、字典是不能切片的---不能使用ELE[1:3]这样的方式
print(ELE['FB'])
