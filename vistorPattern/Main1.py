class Emploee:
    def __init__(self, name):
        self.name = name

    def accept(self, boss):
        pass


class Programer(Emploee):
    def accept(self, boss):
        if type(boss) == CTO:
            boss.visit(self)


class Manager(Emploee):
    def accept(self, boss):
        if type(boss) == CEO:
            boss.visit(self)


class Boss:
    def visit(self, emploee):
        pass


class CEO(Boss):
    def visit(self, manager):
        print('ceo 访问经理', manager.name)


class CTO(Boss):
    def visit(self, programer):
        print('cto 访问码农', programer.name)


class Report:
    def __init__(self):
        self.emploees = []

    def add(self, emp):
        self.emploees.append(emp)

    def remove(self, emp):
        self.emploees.remove(emp)

    def show_report(self, boss):
        for emp in self.emploees:
            emp.accept(boss)


if __name__ == '__main__':
    ceo = CEO()
    cto = CTO()
    report = Report()
    report.add(Programer('小张'))
    report.add(Programer('小林'))
    report.add(Programer('小陈'))

    report.add(Manager('高总'))
    report.add(Manager('郭总'))
    report.add(Manager('林总'))

    report.show_report(ceo)
    report.show_report(cto)