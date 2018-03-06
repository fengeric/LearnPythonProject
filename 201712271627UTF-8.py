# encoding=utf-8
import io

f = io. open("abc.txt", "wt", encoding="utf-8")
f.write(u"Imagine non- English language here")  # 字符串前添加u，输入的就是utf-8模式的文本
f.close()
text = io.open("abc.txt", encoding="utf- 8").read()
print(text)
