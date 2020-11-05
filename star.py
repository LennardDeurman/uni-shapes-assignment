from shape import Shape
import math
from tkinter import Canvas

class Star(Shape):

    def __init__(self, x: int, y: int, width: int, height: int):
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height
        super().__init__()

    def draw(self, canvas: Canvas):
        numPoints = 5
        pts = []
        rx = self.width / 2
        ry = self.height / 2
        cx = self.x + rx
        cy = self.y + ry
        theta = -math.pi / 2
        dtheta = 4 * math.pi / numPoints

        for i in range(0, numPoints + 1):
            pts.append(
                int(round(cx + rx * math.cos(theta))))
            pts.append(
                int(round(cy + ry * math.sin(theta)))
            )
            theta += dtheta

        # we use the '*' syntax here to convert the list of points to function arguments
        canvas.create_line(*pts)
