# __init__() 的神奇之处就在于，如果你在类里定义了它，在创建实例的时候它就能帮你自动地处理很多事情--比如新增实例属性

class CocaCola:
    formula=['caffeine','sugar','water','soda']
    def __init__(self):

        for element in self.formula:
            print('Coke has {} !'.format(element))

    def drink(self):
        print('Energy!')

coke = CocaCola()
coke.drink()
