from abc import ABC , abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(Self):
        pass
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        print(f"The area of this rectangle is {self.length*self.width}")
class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        print(f"The area of this triangle is {0.5*self.base*self.height}")
class Square(Shape):
    def __init__(self,length):
        self.length = length
    def area(self):
        print(f"The area of this square is {self.length*self.length}")

length = float(input("Enter the length of the rectangle:"))
width = float(input("Enter the width of the rectangle:"))
rectangle = Rectangle(length,width)
rectangle.area()
base = float(input("Enter the base of the triangle:"))
height = float(input("Enter the height of the triangle:"))
triangle = Triangle(base,height)
triangle.area()
length = float(input("Enter the length of the square:"))
square = Square(length)
square.area()