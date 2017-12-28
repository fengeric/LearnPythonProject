class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("init SchoolMember:{}".format(self.name))

    def tell(self):
        print('name:"{}" age:"{}"'.format(self.name, self.age))

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("init Teacher{}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('salary:{}'.format(self.salary))

t = Teacher("feng", 25, 1000)
t.tell()
