txt = '''离别家乡岁月多，
近来人事半消磨，
唯有门前镜湖水，
春风不改旧时波'''

# 打开文件以编辑（ 'w'riting）
f = open('mypoem.txt', 'w')
# 向文件中编写文本
f.write(txt)
# 关闭文件
f.close()

# 读取文件的第一种方式
# 如果没有特别指定，将假定启用默认的阅读（'r'ead）模式
f = open('mypoem.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break

    print(line, end=' ')

f.close()
print('----------------------------------------')
# 读取文件的第二种方式
# with语句读取文件
with open('mypoem.txt') as f:
    for line in f:
        print(line)
