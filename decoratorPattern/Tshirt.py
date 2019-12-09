from decoratorPattern.Clothes import Clothes


class Tshirt(Clothes):
    def __init__(self, clothes):
        self.clothes = clothes

    def wear(self):
        self.clothes.wear()
        print('穿上Tshirt')
