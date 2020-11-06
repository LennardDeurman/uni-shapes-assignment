from xml_builder import XmlElement, XmlElementProperties, XmlElementProperty


class SvgBuilder:

    def __init__(self):
        self.root = XmlElement(tag="SVG")
        self.root.props.add_field(XmlElementProperty("xmlns", "http://www.w3.org/2000/svg"))
        self.root.props.add_field(XmlElementProperty("version", "1.1"))

