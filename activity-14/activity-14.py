class Polygon:
    def __init__(self, side_lengths):
        self.side_lengths = side_lengths

    @property
    def num_sides(self):
        return len(self.side_lengths)

    @num_sides.setter
    def num_sides(self, value):
        self.num_sides = value

    @property
    def perimeter(self):
        return sum(self.side_lengths)

    def __str__(self):
        return f"Polygon with {self.num_sides} sides"


class Rectangle(Polygon):
    def __init__(self, height, width):
        self.side_lengths = [height, width, height, width]

    @property
    def area(self):
        return self.side_lengths[0] * self.side_lengths[1]


class Square(Rectangle):
    def __init__(self, side_length):
        self.side_lengths = [side_length, side_length, side_length, side_length]

    @property
    def area(self):
        return self.side_lengths[0] ** 2


r = Rectangle(1, 5)
print(r.area, r.perimeter)

s = Square(5)
print(s.area, s.perimeter)

print(r)
print(s)
