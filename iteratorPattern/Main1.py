from iteratorPattern.Collection1 import Collection1

if __name__ == '__main__':
    iterator = Collection1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).iterator()
    while iterator.has_next():
        print(iterator.next())
