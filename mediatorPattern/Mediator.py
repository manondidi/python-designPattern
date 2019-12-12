class IMediator:
    def speak(self):
        pass


class Mediator(IMediator):
    def __init__(self, house_buyer, house_seller):
        self.house_buyer = house_buyer
        self.house_seller = house_seller

    def speak(self, people, str):
        if (people == self.house_buyer):
            print('买家通过中介对房东说:', str)
        elif (people == self.house_seller):
            print('房东通过中介对买家说:', str)


class People:
    def __init__(self):
        self.mediator = None

    def speak(self, str):
        self.mediator.speak(self, str)


if __name__ == '__main__':
    people1 = People()
    people2 = People()
    mediator = Mediator(people1, people2)
    people1.mediator = mediator
    people2.mediator = mediator
    people2.speak('总价200w')
    people1.speak('便宜点180w卖不卖')
    people2.speak('总价190w,不能再便宜了')
