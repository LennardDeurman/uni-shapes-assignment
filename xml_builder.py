from typing import List

class XmlElementProperty:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value


class XmlElementProperties:

    def __init__(self):
        self.fields = list()

    def add_field(self, field : XmlElementProperty):
        self.fields.append(field)

class XmlElement:

    def __init__(self, tag : str, children : List[XmlElement] = list()):
        self.tag = tag
        self.children = children
        self.props = XmlElementProperties()

