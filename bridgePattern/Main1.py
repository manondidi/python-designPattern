class Shape:
    pass


class Circle(Shape):
    def __init__(self, color):
        self.shape = 'Circle'
        self.color = color.color


class Square(Shape):
    def __init__(self, color):
        self.shape = 'Square'
        self.color = color.color


class Color:
    pass


class Red(Color):
    def __init__(self):
        self.color = 'red'


class Green(Color):
    def __init__(self):
        self.color = 'green'


if __name__ == '__main__':
    red_circle = Circle(Red())
    print(red_circle.__dict__)
