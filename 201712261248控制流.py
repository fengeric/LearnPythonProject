# --------------------if语句--------------------------------------
num = 3
a = int(input('请输入数字'))

if num == a:
    print("aaa")
elif num > a:
    print('bbb')
else:
    print("ccc")
# ----------------------while语句------------------------------------
number = 23
running = True
while running:
    guess = int(input(' Enter an integer : '))
    if guess == number:
        print(' Congratulations, you guessed it. ')
        # 这将导致 while 循环中 止
        running = False
    elif guess < number:
        print(' No, it is a little higher than that. ')
    else:
        print(' No, it is a little lower than that. ')
else:
    print(' The while loop is over. ')
    # 在这里你可以做你想做的任何事
print(' Done')
# ----------------------for循环--------------------------------
for i in range(1, 5):  # 等价for i in [1,2, 3, 4]或for ( int i = 1; i < 5; i++)
    print(i)
else:  # 此句可选可不选，循环结束后 开始执行， 除非程序遇到 了 break 语句 。
    print(' The for loop is over')
# ----------------------break语句--------------------------------
# break 语句 用 以中 断（ Break） 循环语句
# ----------------------continue 语句--------------------------------
# continue 语句 用 以告诉 Python 跳过当 前循环块中 的剩余语句 ， 并继续该循环的下一次迭代。
