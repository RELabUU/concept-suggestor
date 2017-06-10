# This class doesn't handle words that can't be found very well. Thesaurus.com tries to find similarly spelled words and returns those, without an error message or similar. Co-pilot, which is unknown, becomes copulate.

from PyDictionary import PyDictionary

class ThesaurusSynonyms(object):
    """Checks whether words are synonyms using thesaurus.com as a dictionary."""

    TWOWAYCHECK = True # Whether to only check for B == synonym(A) or also for A == synonym(B)

    def __init__(self):
        self.dict = PyDictionary()

    # Checks if the collection has a synonym of the word
    def HasSynonym(self, word, collection):
        # Get the synonyms of "word" once and store them
        self.synonymsOfWord = self.dict.synonym(word)
        print("Synonyms of %s: %s" % (word, self.synonymsOfWord)) # DEBUG

        for cword in collection: 
            if self.IsSynonym(cword, word, self.synonymsOfWord):
                return True
        return False

    # Checks if wordB is a synonym of wordA, and vice-versa if TWOWAYCHECK == True. 
    # synonymsOfWordB is a parameter that can be used for efficiency. I.e. if you want to call this method repeatedly with the same wordB, it's faster to get the synonyms before calling this method.
    def IsSynonym(self, wordA, wordB, synonymsOfWordB = []):
        synonyms = self.dict.synonym(wordA)
        print("Synonyms of %s: %s" % (wordA, synonyms)) # DEBUG

        # Fill the synonymsOfWordB 
        if synonymsOfWordB == [] and self.TWOWAYCHECK is True:
            synonymsOfWordB = self.dict.synonym(wordB)

        # If the collections are identical, the words are expected to be identical.
        if synonyms == synonymsOfWordB:
            return True

        # Check if wordB exists in synonyms of wordA.
        result = wordB.lower() in synonyms
        if result is True:
            return result
        elif self.TWOWAYCHECK is True:
            result = wordA.lower() in synonymsOfWordB
        return result