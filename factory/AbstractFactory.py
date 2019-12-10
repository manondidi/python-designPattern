class Animal:
    def say(self):
        pass


class Bird(Animal):
    def say(self):
        pass


class Duck(Bird):
    def say(self):
        print('i am duck')


class Chicken(Bird):
    def say(self):
        print('i am chicken')


class Fish(Animal):
    def say(self):
        pass


class Shark(Fish):
    def say(self):
        print('i am shark')


class GoldFish(Fish):
    def say(self):
        print('i am goldFish')


class AnimalFactory:
    @staticmethod
    def create():
        pass


class FishFactory(AnimalFactory):
    @staticmethod
    def create(type):
        if type == 'goldFish':
            return GoldFish()
        elif type == 'shark':
            return Shark()


class BirdFactory(AnimalFactory):
    @staticmethod
    def create(type):
        if type == 'duck':
            return Duck()
        elif type == 'chicken':
            return Chicken()


if __name__ == '__main__':
    duck = BirdFactory.create('duck')
    chicken = BirdFactory.create('chicken')

    shark = FishFactory.create('shark')
    goldFish = FishFactory.create('goldFish')

    duck.say()
    chicken.say()
    shark.say()
    goldFish.say()
