import threading


# 双向锁单例模式 线程安全
class Singleton(object):
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return Singleton._instance


def test(number):
    s = Singleton()
    print(str(number) + ": " + str(id(s)))


def main():
    for i in range(10):
        t = threading.Thread(target=test, args=(i,))
        t.start()


if __name__ == '__main__':
    main()
