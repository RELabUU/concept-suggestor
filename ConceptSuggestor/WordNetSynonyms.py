from nltk.corpus import wordnet as wn

class WordNetSynonyms(object):
    """Determines whether two words are synonyms."""

    def __init__(self):
        pass

    def IsSynonym(self, wordA, wordB):
        synsA = wn.synsets(wordA)
        synsB = wn.synsets(wordB)

        match = set(synsA).intersection(synsB)

        if match != set():
            # print("Match: %s" % match) # DEBUG
            return True
        else:
            # print("No match.") # DEBUG
            return False