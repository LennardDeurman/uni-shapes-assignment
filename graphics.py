from abc import ABC, abstractmethod
from tkinter import Canvas
from xml_builder import XmlElement

class Graphics:

    @abstractmethod
    def draw(self, canvas: Canvas):
        pass

    @abstractmethod
    def to_xml(self) -> XmlElement:
        pass