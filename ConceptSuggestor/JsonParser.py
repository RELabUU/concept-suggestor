import json

class JsonParser(object):
    """Parses JSON text to objects and vice-versa"""
    
    FILE = "commit_example.json"

    with open(FILE) as data_file:
        data = json.load(data_file)

    from pprint import pprint
    pprint(data)