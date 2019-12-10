import copy


class Student:
    def __init__(self):
        self.id = None
        self.name = None
        self.age = 0

    def clone(self):
        return copy.deepcopy(self)


if __name__ == '__main__':
    student1 = Student()
    student1.id = '007'
    student1.name = '詹姆斯邦德'
    student1.age = 33

    student2 = student1.clone()
    student1.id = '006'


    print(student1.__dict__)
    print(student2.__dict__)
