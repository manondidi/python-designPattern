class Iterator1:

    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def has_next(self):
        return self.index < len(self.collection.list1)

    def next(self):
        self.index += 1
        return self.collection.list1[self.index - 1]
