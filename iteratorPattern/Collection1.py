from iteratorPattern.Iterator1 import Iterator1


class Collection1:
    def __init__(self, list1):
        self.list1 = list1

    def iterator(self):
        return Iterator1(self)
