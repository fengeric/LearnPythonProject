def mkdir(path):
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip('\\')

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.mkdir(path)
        print(path + '创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + '目录已存在')
        return False


# def create_folder(folder_name):
#     folder_path = 'C:/Users/Administrator/Desktop/' + folder_name + '/'
#     mkdir(folder_path)


def create_text(folder_name, file_name, msg):
    folder_path = 'C:/Users/Administrator/Desktop/' + folder_name + '/'

    mkdir(folder_path)

    full_path = folder_path + file_name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print(folder_name + '-' + file_name + '-Done')


for i in range(1, 11):
    create_text('haha', str(i), str(i))
