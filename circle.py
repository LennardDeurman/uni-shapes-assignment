from shape import Shape
from tkinter import Canvas
from xml_builder import XmlElement, XmlElementProperty
from svg_builder import SvgBuilder
from graphics import Graphics


class CircleGraphics(Graphics):

    def __init__(self, circle_shape):
        self.circle_shape = circle_shape

    def draw(self, canvas: Canvas):
        canvas.create_oval(self.circle_shape.x - self.circle_shape.radius, self.circle_shape.y - self.circle_shape.radius,
                           self.circle_shape.x + self.circle_shape.radius, self.circle_shape.y + self.circle_shape.radius)

    def to_xml(self) -> XmlElement:
        svg_builder = SvgBuilder()
        circle_element = XmlElement("circle")
        circle_element.props.fields.append(XmlElementProperty(key="cx", value=self.circle_shape.x))
        circle_element.props.fields.append(XmlElementProperty(key="cy", value=self.circle_shape.y))
        circle_element.props.fields.append(XmlElementProperty(key="r", value=self.circle_shape.radius))
        svg_builder.root.children.append(circle_element)
        return svg_builder.root



class Circle(Shape):

    def __init__(self, x: int, y: int, radius: int):
        self.x: int = x
        self.y: int = y
        self.radius: int = radius
        super().__init__()

    def create_graphics(self) -> Graphics:
        return CircleGraphics(self)

    def draw(self, canvas: Canvas):
        self.graphics.draw(canvas)
    
    def to_xml(self) -> XmlElement:
        return self.graphics.to_xml()

    def name(self) -> str:
        return "circle"