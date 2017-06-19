from nltk.corpus import wordnet as wn

class WordNetSimilarity(object):
    """Uses WordNet to determine whether words are synonyms"""

    # These two methods use incorrect ways of determining synonyms. Better: calculate similarity, and use a threshold.
    """
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
    """

    def GetSimilarity(self, wordA, wordB):
        if wordA == wordB: # wup_similarity is coded in such a way that identical words don't necessarily return a similarity of 1, so we manually force that here.
            return 1

        wa = wn.synsets(wordA)
        wb = wn.synsets(wordB)

        if wordA == "Passenger" and wordB == "Passenger":
            print("%s\n%s" % (wa, wb))

        similarity = 0
        if wa and wb:
            similarity = wa[0].wup_similarity(wb[0])

        #print("WordNet: Similarity between \"%s\" and \"%s\": %s" % (wordA, wordB, similarity)) # DEBUG
        return similarity

    def GetMaxSimilarity(self, word, collection):
        wa = wn.synsets(word)
        
        maxSimilarity = 0
        maxSimWord = "NONE" # DEBUG
        if wa:
            for wordB in collection:
                if word == wordB: # wup_similarity is coded in such a way that identical words don't necessarily return a similarity of 1, so we manually force that here.
                    maxSimilarity = 1
                    maxSimWord = wordB
                    break
                wb = wn.synsets(wordB)
                if wb:
                    similarity = wa[0].wup_similarity(wb[0])
                    if similarity > maxSimilarity:
                        maxSimilarity = similarity
                        maxSimWord = wordB # DEBUG

        print("WordNet: Maximum similarity %s found to word \"%s\"" % (maxSimilarity, maxSimWord)) # DEBUG
        return maxSimilarity