from abc import ABC, abstractmethod
from tkinter import Canvas


class XmlElementProperty:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value


class XmlElementProperties:

    def __init__(self):
        self.fields = list()

    def add_field(field : XmlElementProperty):
        self.fields.add(field)

class XmlElement:

    def __init__(self, tag : str, children : List[XmlElement] = list()):
        self.tag = tag
        self.children = children
        self.props = XmlElementProperties()


class SvgBuilder:

    def __init__(self):
        self.root = XmlElement(tag="SVG")
        self.root.props.add_field(XmlElementProperty("xmlns", "http://www.w3.org/2000/svg"))
        self.root.props.add_field(XmlElementProperty("version", "1.1"))

    
class Graphics:

    @abstractmethod
    def draw(self, canvas : Canvas):
        pass
    
    @abstractmethod
    def generate_svg(self) -> Svg:
        pass

class Shape(ABC):

    @abstractmethod
    def draw(self, canvas: Canvas):
        pass
