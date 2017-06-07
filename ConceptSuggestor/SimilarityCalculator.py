class SimilarityCalculator(object):
    """Calculates the similarity of two words using a variety of methods."""

    def __init__(self, threshold, useWordVectors = False, wordVectorWeight = 0, useThesaurus = False, thesaurusWeight = 0, useWordNet = False, wordNetWeight = 0, totalWeight = 0):
        self.useWordVectors = useWordVectors
        if self.useWordVectors is True:
            from SpacySimilarity import SpacySimilarity
            self.ss = SpacySimilarity()
            self.wordVectorWeight = wordVectorWeight

        self.useThesaurus = useThesaurus
        if self.useThesaurus is True:
            from ThesaurusSynonyms import ThesaurusSynonyms
            self.ts = ThesaurusSynonyms()
            self.thesaurusWeight = thesaurusWeight

        self.useWordNet = useWordNet
        if self.useWordNet is True:
            from WordNetSimilarity import WordNetSimilarity
            self.wns = WordNetSimilarity()
            self.wordNetWeight = wordNetWeight

        self.totalWeight = totalWeight

    # Returns the similarity of two words.
    def GetSimilarity(self, wordA, wordB):
        total = 0

        if self.useWordVectors is True:
            spacySimilarity = self.ss.GetSimilarity(wordA, wordB)
            spacySimilarity *= self.wordVectorWeight
            total += spacySimilarity

        if self.useThesaurus is True:
            thesaurus = int(self.ts.IsSynonym(wordA, wordB))
            thesaurus *= self.thesaurusWeight
            total += thesaurus

        if self.useWordNet is True:
            wordNet = self.wns.GetSimilarity(wordA, wordB)
            wordNet *= self.wordNetWeight
            total += wordNet

        print("Total: %s + %s + %s = %s out of %s" % (spacySimilarity, thesaurus, wordNet, total, self.totalWeight)) # DEBUG

        total /= self.totalWeight

        return total

    # Returns the maximum similarity of a word to all words in the collection. Individual methods can use different words for maximum similarity. I.e. spacy finds A and C to have maximum similarity, and returns that value, and WordNet finds A and B to have maximum similarity, and returns that value. This means that the maximum similarity is not between two words, but between a word and various words in the collection.
    def GetMaxSimilarity(self, word, collection):
        total = 0

        if self.useWordVectors is True:
            spacySimilarity = self.ss.GetMaxSimilarity(word, collection)
            spacySimilarity *= self.wordVectorWeight
            total += spacySimilarity

        if self.useThesaurus is True:
            thesaurus = int(self.ts.HasSynonym(word, collection))
            thesaurus *= self.thesaurusWeight
            total += thesaurus

        if self.useWordNet is True:
            wordNet = self.wns.GetMaxSimilarity(word, collection)
            wordNet *= self.wordNetWeight
            total += wordNet

        print("Total: %s + %s + %s = %s out of %s" % (spacySimilarity, thesaurus, wordNet, total, self.totalWeight)) # DEBUG

        total /= self.totalWeight

        return total