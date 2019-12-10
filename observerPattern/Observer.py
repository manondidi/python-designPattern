from observerPattern.Obj import Obj


class Observer:
    def __init__(self, obj):
        self.obj = obj

    def update(self):
        print("观察" + self.obj.key)
