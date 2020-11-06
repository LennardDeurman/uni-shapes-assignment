from shape import Shape
import math
from tkinter import Canvas
from xml_builder import XmlElement, XmlElementProperty
from svg_builder import SvgBuilder
from graphics import Graphics

class StarGraphics(Graphics):


    def __init__(self, star_shape):
        self.star_shape = star_shape

    def draw(self, canvas: Canvas):
        numPoints = 5
        pts = []
        rx = self.star_shape.width / 2
        ry = self.star_shape.height / 2
        cx = self.star_shape.x + rx
        cy = self.star_shape.y + ry
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

    def to_xml(self) -> XmlElement:
        svg_builder = SvgBuilder()
        polygon_element = XmlElement("polygon")
        polygon_element.props.fields.append(XmlElementProperty(key="points", value="100,10 40,198 190,78 10,78 160,198"))
        svg_builder.root.children.append(polygon_element)
        return svg_builder.root

class Star(Shape):

    def __init__(self, x: int, y: int, width: int, height: int):
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height
        super().__init__()

    def create_graphics(self) -> Graphics:
        return StarGraphics(self)

    def draw(self, canvas: Canvas):
        self.graphics.draw(canvas)

    def to_xml(self) -> XmlElement:
        return self.graphics.to_xml()
    
    def name(self) -> str:
        return "star"
