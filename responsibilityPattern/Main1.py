class Document:
    def __init__(self, level, name):
        self.level = level
        self.name = name


class IEmployee:
    def deal_document(self, document):
        pass


class Employee(IEmployee):
    def __init__(self, name, level, manager=None):
        self.name = name
        self.level = level
        self.manager = manager

    def deal_document(self, document):
        if self.level >= document.level:
            print('文件', document.name, '被', self.name, '处理了')
        elif self.manager is not None:
            self.manager.deal_document(document)
        else:
            print('文件级别太高,无人可以处理')


if __name__ == '__main__':
    boss = Employee('王思聪', 99)
    manager = Employee('陈经理', 8, boss)
    emp = Employee('小张', 1, manager)

    document1 = Document(1, '普通文件')
    document7 = Document(7, '高级文件')
    document88 = Document(88, '机密文件')

    emp.deal_document(document1)
    emp.deal_document(document7)
    emp.deal_document(document88)
