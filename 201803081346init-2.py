class CocaCola:
    formula = ['caffeine', 'sugar', 'water', 'soda']

    def __init__(self, logo_name):
        self.local_logo = logo_name

    def drink(self):
        print('Enery !')


coke = CocaCola('可口可乐')

print(coke.local_logo)
coke.drink()


class TestA:
    attr = 1

obj_a = TestA()
obj_b = TestA()

obj_a.attr = 42
print(obj_b.attr)
