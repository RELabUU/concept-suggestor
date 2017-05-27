import json

class JsonParser(object):
    """Parses JSON text to objects and vice-versa"""

    def LoadFile(self, file):
        with open(file) as data_file:
            data = json.load(data_file)

        from pprint import pprint
        #pprint(data)

        newitems = []

        for item in data:
            if(item["op"] == "add_element"):
                newitems.append(item["label"])
            else:
                print("Do not understand commit message: %s" % item["op"])

        return newitems
    
    def MakeFile(self, data, file):
        with open(file, "w") as data_file:
            json.dump(data, data_file)