from abc import ABC, abstractmethod
from tkinter import Canvas
from xml_builder import XmlElement
from graphics import Graphics

class Shape(ABC):

    def __init__(self):
        self.graphics : Graphics = self.create_graphics()

    @abstractmethod
    def draw(self, canvas: Canvas):
        pass

    @abstractmethod
    def to_xml(self) -> XmlElement:
        pass
    
    @abstractmethod
    def create_graphics(self) -> Graphics:
        pass
    
    @abstractmethod
    def name(self) -> str:
        pass