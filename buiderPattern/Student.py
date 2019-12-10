class Student:
    def __init__(self):
        self.id = None
        self.name = None
        self.age = 0

    @staticmethod
    def builder():
        return Builder()


class Builder:
    def __init__(self):
        self.student = Student()

    def setId(self, id):
        self.student.id = id
        return self

    def setName(self, name):
        self.student.name = name
        return self

    def setAge(self, age):
        self.student.age = age
        return self

    def build(self):
        return self.student


if __name__ == '__main__':
    student = Student.builder().setAge(9).setId('007').setName('詹姆斯邦德').build()
    print(student.__dict__)