try:
    from typing import override
except ImportError:
    from typing_extensions import override

print("="*60)
print("Section 8 : Override")
print("="*60)

class Shape:
    def area(self) -> float:
        return 0.0
    def perimeter(self) -> float:
        return 0.0

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @override
    def area(self) -> float:
        return self.width * self.height

    @override
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

rectangle = Rectangle(10,10)
print(rectangle.area())
print(rectangle.perimeter())