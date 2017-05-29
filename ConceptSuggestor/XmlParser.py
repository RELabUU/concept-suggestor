import xml.etree.ElementTree as ET

class XmlParser(object):
    """Parses XML files."""

    def LoadFile(self, file):
        tree = ET.parse(file)
        root = tree.getroot()
        namespaces = {"UML": "omg.org/UML1.3"}
        classes = []
        for node in tree.findall(".//UML:Class", namespaces):
            name = node.attrib.get("name")
            classes.append(name)
        return classes