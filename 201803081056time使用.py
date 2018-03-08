import time

arr = []
t0 = time.clock()
for i in range(1, 20000):
    arr.append(i)
print(time.clock() - t0, 'seconds process time')

t1 = time.clock()
b = [i for i in range(1, 20000)]
print(time.clock() - t1, 'seconds process time')
