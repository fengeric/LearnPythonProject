#Python 中 有四种内 置的数据结构——列 表（ List） 、 元组（ Tuple） 、 字典（ Dictionary） 和集合（ Set）
#列 表（ List）
shoplist = [' apple' , ' mango' , ' carrot' , ' banana' ]
print( ' I have' , len( shoplist) , ' items to purchase. ' )
for item in shoplist:
    print( item)
shoplist. append( ' rice' )
print( ' My shopping list is now' , shoplist)
shoplist. sort( )
print( ' My shopping list is now' , shoplist)
print( ' The first item I will buy is' , shoplist[0] )
del shoplist[0]
print( ' My shopping list is now' , shoplist)
print('---------------------------------------')
#元组（ Tuple）
zoo = ( ' python' , ' elephant' , ' penguin' )
print( ' Number of animals in the zoo is' , len( zoo) )
new_zoo = (' monkey' , ' camel' , zoo)
print( ' Number of cages in the new zoo is' , len( new_zoo) )
print( ' All animals in new zoo are' , new_zoo)
print( ' Animals brought from old zoo are' , new_zoo[2] )
print( ' Last animal brought from old zoo is' , new_zoo[2] [2] )
print( ' Number of animals in the new zoo is' ,
len( new_zoo) - 1+len( new_zoo[2] ) )
print('---------------------------------------')
#字典
# “ab”是地址（ Address） 簿（ Book） 的缩写
ab = {
    ' Swaroop' : ' swaroop@swaroopch. com' ,
    ' Larry' : ' larry@wall. org' ,
    ' Matsumoto' : ' matz@ruby- lang. org' ,
    ' Spammer' : ' spammer@hotmail. com'
 }
print( "Swaroop' s address is", ab[' Swaroop' ] )

# 删 除一对键值—值配对
del ab[' Spammer' ]

print( ' \nThere are {} contacts in the address- book\n' . format( len( ab) ) )

for name, address in ab. items( ) :
    print( ' Contact {} at {}' . format( name, address) )

# 添加一对键值—值配对
ab[' Guido' ] = ' guido@python. org'

if ' Guido' in ab:
    print( "\nGuido' s address is", ab[' Guido' ] )
print('---------------------------------------')
#序列
#>>> list = ['a','b','c','d','e']
#>>> print(list[1:3])
#['b', 'c']
#>>> print(list[2:])
#['c', 'd', 'e']
#>>> print(list[1:-1])#使用负数时位置将从序列末端开始计算。
#['b', 'c', 'd']
#>>> print(list[2:-1])
#['c', 'd']
#>>> print(list[2:-2])
#['c']
#>>> print(list[:])
#['a', 'b', 'c', 'd', 'e']
print('---------------------------------------')
#集合
#>>> bri = set( [' brazil' , ' russia' , ' india' ] )
#>>> ' india' in bri
#True
#>>> ' usa' in bri
#False
#>>> bric = bri. copy( )
#>>> bric. add( ' china' )
#>>> bric. issuperset( bri)
#True
#>>> bri. remove( ' russia' )
#>>> bri & bric # OR bri. intersection( bric)
#{' brazil' , ' india' }
print('---------------------------------------')
#引用
#>>> list = ['a','b','c','d','e','f']
#>>> mylist = list#重要，两个列表指向同一个对象，会相互影响
#>>> del list[0]
#>>> print(list)
#['b', 'c', 'd', 'e', 'f']
#>>> print(mylist)
#['b', 'c', 'd', 'e', 'f']
#>>> mylist = list[:]#重要，两个对象，不会相互影响
#>>> del mylist[0]
#>>> print(list)
#['b', 'c', 'd', 'e', 'f']
#>>> print(mylist)
#['c', 'd', 'e', 'f']
#>>> del list[0]
#>>> print(mylist)
#['c', 'd', 'e', 'f']
