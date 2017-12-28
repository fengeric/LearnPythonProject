class Person:
    def ss(self):
        print("hell world")

p = Person()
p.ss()
#-----------------------------------------------
class Person2:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print("hello world", self.name)

p2 = Person2("feng");
p2.say_hi()
