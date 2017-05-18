from PyDictionary import PyDictionary

class DictionarySynonyms(object):
    """description of class"""

    TWOWAYCHECK = True # Whether to only check for B == synonym(A) or also for A == synonym(B)

    def __init__(self):
        self.dict = PyDictionary()

    # Checks if the collection has a synonym of the word
    def HasSynonym(self, collection, word):
        # Get the synonyms of "word" once and store them
        self.synonymsOfWord = []
        if(self.TWOWAYCHECK is True):
            self.synonymsOfWord = self.dict.synonym(word)
            print("Synonyms of %s: %s" % (word, self.synonymsOfWord)) # DEBUG

        for cword in collection:
            if self.IsSynonym(cword, word, self.synonymsOfWord):
                return True
        return False

    # Checks if wordB is a synonym of wordA, and vice-versa if TWOWAYCHECK == True
    def IsSynonym(self, wordA, wordB, synonymsOfWordB):
        synonyms = self.dict.synonym(wordA)
        print("Synonyms of %s: %s" % (wordA, synonyms)) # DEBUG
        result = wordB.lower() in synonyms
        if result is True:
            return result
        elif self.TWOWAYCHECK is True:
            result = wordA.lower() in synonymsOfWordB
        return result