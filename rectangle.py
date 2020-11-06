from shape import Shape
from tkinter import Canvas
from xml_builder import XmlElement, XmlElementProperty
from svg_builder import SvgBuilder
from graphics import Graphics

class RectangleGraphics(Graphics):

    def __init__(self, rectangle_shape):
        self.rectangle_shape = rectangle_shape

    def draw(self, canvas: Canvas): 
        canvas.create_line(self.rectangle_shape.x, self.rectangle_shape.y,
                           self.rectangle_shape.x + self.rectangle_shape.width, self.rectangle_shape.y,
                           self.rectangle_shape.x + self.rectangle_shape.width, self.rectangle_shape.y + self.rectangle_shape.height,
                           self.rectangle_shape.x, self.rectangle_shape.y + self.rectangle_shape.height,
                           self.rectangle_shape.x, self.rectangle_shape.y)

    def to_xml(self) -> XmlElement:
        svg_builder = SvgBuilder()
        rect_element = XmlElement("rect")
        rect_element.props.fields.append(XmlElementProperty(key="x", value=self.rectangle_shape.x))
        rect_element.props.fields.append(XmlElementProperty(key="y", value=self.rectangle_shape.y))
        rect_element.props.fields.append(XmlElementProperty(key="width", value=self.rectangle_shape.width))
        rect_element.props.fields.append(XmlElementProperty(key="height", value=self.rectangle_shape.height))
        svg_builder.root.children.append(rect_element)
        return svg_builder.root


class Rectangle(Shape):

    def __init__(self, x: int, y: int, width: int, height: int):
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height
        super().__init__()

    def create_graphics(self) -> Graphics:
        return RectangleGraphics(self)

    def draw(self, canvas: Canvas):
        self.graphics.draw(canvas)
    
    def to_xml(self) -> XmlElement:
        return self.graphics.to_xml()
    
    def name(self) -> str:
        return "rectangle"
