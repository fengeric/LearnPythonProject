# -------------------------------------------------------------
# --------------------创建文件-----------------------------------------
def text_create(name, msg):
    desktop_path = 'C:/Users/Administrator/Desktop'
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print('Done')


text_create('mytext', 'This is content')


# ---------------------过滤替换关键词----------------------------------------
def text_filter(word, senword='lame', replaceword='Awesome'):
    return word.replace(senword, replaceword)


print(text_filter('python is lame!'))
