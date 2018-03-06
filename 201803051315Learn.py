import os

print(os.getcwd())
# -----------打印数据类型-----------------
a = 'c'
print(type(a))
# -----------隐藏手机号码-------------------
phone_num = '185 4567 8987'
hide_num = phone_num.replace(phone_num[:9], '*' * 9)
print(hide_num)
# -----------format的用法------------------
print('{} a word she can get what she {} for!'.format('With', 'came'))
print('{preposition} a word she can get what she {verb} for!'.format(preposition = 'With', verb = 'came'))
print('{0} a word she can get what she {1} for!'.format('With', 'came'))
print('{1} a word she can get what she {0} for!'.format('With', 'came'))
