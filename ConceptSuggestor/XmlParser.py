class XmlParser(object):
    """Parses XML files."""

    import xmltodict

    def LoadFile(file):
        with open(file) as data_file:
            data = xmltodict.parse(data_file.read())

        print("Currently not supported.")