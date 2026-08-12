import math


class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def set_width(self, width: int) -> int:
        self.width = width
        return self.width

    def set_height(self, height: int) -> int:
        self.height = height
        return self.height

    def get_area(self) -> int:
        self.area = self.width * self.height
        return self.area

    def get_perimeter(self) -> int:
        self.perimeter = 2 * (self.width + self.height)
        return self.perimeter

    def get_diagonal(self) -> float:
        self.diagonal = math.sqrt((self.width ** 2) + (self.height ** 2))
        return self.diagonal

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return f"Too big for picture."
        else:
            return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape) -> int:
        horizontal = self.width // shape.width
        vertical = self.height // shape.height
        return horizontal * vertical


    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side: int) -> None:
        self.side = side
        self.height = side
        self.width = side

    def set_width(self, side: int) -> int:
        self.width = side
        self.height = side
        self.side = side
        return self.width

    def set_height(self, side: int) -> int:
        self.height = side
        self.width = side
        self.side = side
        return self.height

    def set_side(self, side: int) -> int:
        self.side = side
        self.height = side
        self.width = side
        return self.side

    def __str__(self) -> str:
        return f"Square(side={self.side})"
    
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))