from shape import Shape
from tkinter import Canvas


class Circle(Shape):

    def __init__(self, x: int, y: int, radius: int):
        self.x: int = x
        self.y: int = y
        self.radius: int = radius
        super().__init__()

    def draw(self, canvas: Canvas):
        canvas.create_oval(self.x - self.radius, self.y - self.radius,
                           self.x + self.radius, self.y + self.radius)
