class Animal:
    def say(self):
        pass


class Bird(Animal):
    def say(self):
        print('i am bird')


class Fish(Animal):
    def say(self):
        print('i am fish')


class AnimalFactory:
    @staticmethod
    def create():
        pass


class FishFactory(AnimalFactory):
    @staticmethod
    def create():
        return Fish()


class BirdFactory(AnimalFactory):
    @staticmethod
    def create():
        return Bird()


# 工厂方法
if __name__ == '__main__':
    fish = FishFactory.create()
    fish.say()

    bird = BirdFactory.create()
    bird.say()
