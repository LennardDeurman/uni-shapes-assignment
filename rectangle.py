from shape import Shape
from tkinter import Canvas

class Rectangle(Shape):

    def __init__(self, x: int, y: int, width: int, height: int):
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height
        super().__init__()

    def draw(self, canvas: Canvas):
        canvas.create_line(self.x, self.y,
                           self.x + self.width, self.y,
                           self.x + self.width, self.y + self.height,
                           self.x, self.y + self.height,
                           self.x, self.y)
