from observerPattern.Obj import Obj
from observerPattern.Observer import Observer

if __name__ == '__main__':
    obj = Obj()
    observer1 = Observer(obj)
    observer2 = Observer(obj)
    obj.add_observer(observer1)
    obj.add_observer(observer2)
    obj.key = 'first'
    obj.notify()
    obj.key = 'second'
    obj.notify()
    obj.remove_observer(observer1)
    obj.remove_observer(observer2)
