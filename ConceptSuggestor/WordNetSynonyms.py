from nltk.corpus import wordnet as wn

class WordNetSynonyms(object):
    """Uses WordNet to determine whether words are synonyms"""

    # Checks if the collection has a synonym of the word
    def HasSynonym(self, word, collection):
        for cword in collection:
            print("Comparing %s and %s" % (cword, word))
            if self.IsSynonym(cword, word):
               return True
        return False

    def IsSynonym(self, wordA, wordB):
        synonyms = []
        for syn in wn.synsets(wordA):
            for l in syn.lemmas():
                synonyms.append(l.name())
        print("Synonyms of %s: %s" % (wordA, synonyms))
        result = wordB.lower() in synonyms
        return result