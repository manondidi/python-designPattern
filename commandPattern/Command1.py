from commandPattern.ICommand import ICommand


class Command1(ICommand):
    def __init__(self, excuter):
        self.excuter = excuter

    def excute(self):
        self.excuter.do_something1()
