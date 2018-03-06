import cmath


# ---------------------------------------------
# ------------摄氏度转华氏摄氏度---------------------------------


def fahrenheit_converter(C):
    fahrenheit = C * 9 / 5 + 32
    return str(C) + '℃ = ' + str(fahrenheit) + '℉'


info = fahrenheit_converter(35)
print(info)


# --------------g转kg-------------------------------

def g2kg(gw):
    kgw = gw / 1000
    return str(gw) + 'g = ' + str(kgw) + 'kg'


print(g2kg(1500))


# --------------计算直角三角形斜边长(需要导入math函数)-------------------------------


def calculate_side_len(x, y):
    z = cmath.sqrt(x ** 2 + y ** 2)
    return 'The right triangle third side\'s length is' + str(z)


print(calculate_side_len(3, 4))
