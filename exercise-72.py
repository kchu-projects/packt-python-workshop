class Circle:
    is_shape = True

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color


first_circle = Circle(2, "blue")
second_circle = Circle(3, "red")

print(first_circle.color)
print(second_circle.color)
print(first_circle.is_shape)
