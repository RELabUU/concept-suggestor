import json

class JsonParser(object):
    """Reads and writes JSON files."""

    # Loads a JSON file and returns the data
    def LoadFile(self, file):
        with open(file) as data_file:
            data = json.load(data_file)
        
        return data

    # Loads a commit JSON file and returns a list of new concepts.
    def LoadCommit(self, file):
        data = self.LoadFile(file)

        newitems = []

        for item in data:
            if item["op"] == "add_element":
                newitems.append(item["label"])
            else:
                print("Do not understand commit message: %s" % item["op"])

        return newitems
    
    def LoadConcepts(self, file):
        data = self.LoadFile(file)

        items = []

        for item in data:
            items.append(item)

        return items

    # Writes a list to a JSON file.
    def MakeFile(self, data, file):
        with open(file, "w") as data_file:
            json.dump(data, data_file)