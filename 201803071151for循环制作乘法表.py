# ---------for循环(方式一)-----------------------------
for letter in 'hello world':
    print(letter)

print('-------------------------')
# ---------for循环(方式二)-----------------------------
for num in range(1, 10):
    print(num)
print('-------------------------')
# ---------九九乘法表(方式一)-----------------------------
for i in range(1, 10):
    for j in range(1, 10):
        if j >= i:
            print(str(i) + '*' + str(j) + '=' + str(i * j), end=' ')
            # print('{} * {} = {}'.format(i, j, i * j))
    print('\n')
print('-------------------------')
# ---------九九乘法表(方式二)-----------------------------
for i in range(1, 10):
    for j in range(1, 10):
        if i >= j:
            print(str(j) + '*' + str(i) + '=' + str(i * j), end=' ')
    print('\n')
