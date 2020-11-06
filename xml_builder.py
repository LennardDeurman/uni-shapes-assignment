from typing import List

class XmlElementProperty:
    
    def __init__(self, key, value):
        self.key = key
        self.value = str(value)


class XmlElementProperties:

    def __init__(self):
        self.fields = list()

class XmlWriter:

    def props_str(self, props) -> str:
        prop_strs = list()
        for field in props.fields:
            prop_strs.append("{0}=\"{1}\"".format(field.key, field.value))
        return " ".join(prop_strs)
        

    def start_tag(self, tag, props) -> str:
        return "<{0} {1}>".format(tag, self.props_str(props))
    
    def end_tag(self, tag) -> str:
        return "</{0}>".format(tag)

class XmlElement:

    def __init__(self, tag : str):
        self.tag = tag
        self.children = list()
        self.props = XmlElementProperties()

    def encode(self) -> str:
        writer = XmlWriter()

        start_tag = writer.start_tag(self.tag, self.props)
        end_tag = writer.end_tag(self.tag)
        inner_content = ""

        for child in self.children:
            inner_content += child.encode()

        tag = "{0}{1}{2}".format(start_tag, inner_content, end_tag)
        return tag


