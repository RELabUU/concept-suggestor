from PyDictionary import PyDictionary

class DictionarySynonyms(object):
    """description of class"""

    TWOWAYCHECK = True # Whether to only check for B == synonym(A) or also for A == synonym(B)

    def __init__(self):
        self.dict = PyDictionary()

    # Checks if the collection has a synonym of the word
    def HasSynonym(self, collection, word):
        for cword in collection:
            if self.IsSynonym(cword, word):
                return True
        return False

    # Checks if wordB is a synonym of wordA, and vice-versa if TWOWAYCHECK == True
    def IsSynonym(self, wordA, wordB):
        synonyms = self.dict.synonym(wordA)
        print("Synonyms of %s: %s" % (wordA, synonyms)) # DEBUG
        result = wordB.lower() in synonyms
        if result is True:
            return result
        elif self.TWOWAYCHECK is True:
            synonyms = self.dict.synonym(wordB)
            print("Synonyms of %s: %s" % (wordB, synonyms)) # DEBUG
            result = wordA.lower() in synonyms
        return result