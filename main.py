class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


rect = Rectangle(4, 5)
print(f"Rectangle Area: {rect.area()}")
print(f"Rectangle Perimeter: {rect.perimeter()}")


sq = Square(4)
print(f"Square Area: {sq.area()}")
print(f"Square Perimeter: {sq.perimeter()}")