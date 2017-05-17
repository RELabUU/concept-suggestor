from PyDictionary import PyDictionary

class DictionarySynonyms(object):
    """description of class"""
    def __init__(self):
        self.dict = PyDictionary()

    # Checks if the collection has a synonym of the word
    def HasSynonym(self, collection, word):
        for cword in collection:
            if self.IsSynonym(cword, word):
                return True
        return False

    def IsSynonym(self, wordA, wordB):
        synonyms = self.dict.synonym(wordA)
        print("Synonyms of %s: %s" % (wordA, synonyms)) # DEBUG
        return wordB.lower() in synonyms