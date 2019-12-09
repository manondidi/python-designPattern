from decoratorPattern.Boy import Boy
from decoratorPattern.Tshirt import Tshirt
from decoratorPattern.Dress import Dress

def main():
    boy = Boy()
    dress = Dress(boy)
    tshirt = Tshirt(dress)
    tshirt.wear()


if __name__ == '__main__':
    main()
