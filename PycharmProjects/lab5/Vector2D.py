class Vector2D:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self = self + other
        return self

    def __str__(self):
        return f'({self.x}, {self.y})'
