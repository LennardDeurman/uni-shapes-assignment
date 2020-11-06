from xml_builder import XmlElement, XmlElementProperties, XmlElementProperty


class SvgBuilder:

    def __init__(self):
        self.root = XmlElement(tag="svg")
        self.root.props.fields.append(XmlElementProperty("xmlns", "http://www.w3.org/2000/svg"))
        self.root.props.fields.append(XmlElementProperty("version", "1.1"))

