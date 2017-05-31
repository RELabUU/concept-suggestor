class CollectionManager(object):
    """Manages collections of concepts"""
    
    def __init__(self):
        self.collections = {}

    # Loads several JSON files using a dictionary that is passed to the method.
    def LoadCollections(self, collections):
        from JsonParser import JsonParser
        jp = JsonParser()

        for collection in collections:
            self.collections[collection] = jp.LoadFile(collections[collection])

    # Adds one or multiple words to an existing collection. Note: "collection" is the key to the dictionary, not an actual collection.
    def AddToCollection(self, collection, words):
        if type(words) is list:
            self.collections[collection].extend(words)
        else:
            self.collections[collection].append(words)

    # Removes one or multiple words from an existing collection. Note: "collection" is the key to the dictionary, not an actual collection.
    def RemoveFromCollection(self, collection, words):
        if type(words) is list:
            for word in words:
                self.collections[collection].remove(word)
        else:
            self.collections[collection].remove(word)

    def WordInCollection(self, collection, word):
        return word in self.collections[collection]

    # Returns a number between 0 and 1 denoting in how many collections the word occurs.
    def FrequencyOfWord(self, word):
        collectionCount = len(self.collections.keys())
        foundCount = 0

        for collection in self.collections:
            if word in self.collections[collection]:
                foundCount += 1

        return foundCount / collectionCount