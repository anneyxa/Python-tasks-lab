from Utils import validate_angle, validate_ratio, check_size_number, validate_size_expected
from Vector2D import Vector2D


class Figure:
    COLORS = {'black', 'white', 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow'}

    def __init__(self, name, *size):
        self.name = name
        self.size = check_size_number(list(size))
        self.center = Vector2D(0, 0)
        self.border_color = 'black'
        self.background_color = 'white'
        self.angle = 0  # when it comes to the circle, now angle doesn't make sense, but if it "in future" had sth
        # inside, like a complex filling/texture, then angle would have sense. In any other type of figure, I believe
        # that angle makes sense

    def move(self, x, y):
        self.center += Vector2D(x, y)

    def scale(self, ratio):
        ratio = validate_ratio(ratio)
        self.size *= ratio

    def rotate(self, angle):
        angle = validate_angle(angle)
        self.angle = 360 % (self.angle + int(angle))

    def set_border_color(self, color):
        self.border_color = self.validate_color(color)

    def set_background_color(self, color):
        self.background_color = self.validate_color(color)

    def validate_color(self, color):
        if color in self.COLORS:
            return color
        else:
            raise ValueError(f'This color is not supported. Supported colors: {Figure.COLORS}')

    def __str__(self):
        return f'name: {self.name}; border color: {self.border_color}; background color: {self.background_color}; ' \
               f'center: {self.center}; rotation: {self.angle}; size: {self.size} '


class Circle(Figure):
    def __init__(self, name, *size):
        size = validate_size_expected(size, 1)
        super().__init__(name, *size)

    def __str__(self):
        return f'Circle: {super().__str__()}'


class Square(Figure):
    def __init__(self, name, *size):
        size = validate_size_expected(size, 1)
        super().__init__(name, *size)

    def __str__(self):
        return f'Square ({super().__str__()})'


class Rectangle(Figure):
    def __init__(self, name, *size):
        size = validate_size_expected(size, 2)
        super().__init__(name, *size)

    def __str__(self):
        return f'Rectangle ({super().__str__()})'


class Triangle(Figure):
    def __init__(self, name, *size):
        size = validate_size_expected(size, 3)
        super().__init__(name, *size)

    def __str__(self):
        return f'Triangle ({super().__str__()})'
