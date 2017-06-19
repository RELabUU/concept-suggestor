class SimilarityCalculator(object):
    """Calculates the similarity of two words using a variety of methods."""

    def __init__(self, useWordVectors = False, wordVectorWeight = 0, useWordNet = False, wordNetWeight = 0, totalWeight = 0):
        self.useWordVectors = useWordVectors
        if self.useWordVectors is True:
            from SpacySimilarity import SpacySimilarity
            self.ss = SpacySimilarity()
            self.wordVectorWeight = wordVectorWeight

        self.useWordNet = useWordNet
        if self.useWordNet is True:
            from WordNetSimilarity import WordNetSimilarity
            self.wns = WordNetSimilarity()
            self.wordNetWeight = wordNetWeight

        self.totalWeight = totalWeight

    # Returns the similarity of two words.
    def GetSimilarity(self, wordA, wordB):
        total = 0

        spacySimilarity = 0
        if self.useWordVectors is True:
            spacySimilarity = self.ss.GetSimilarity(wordA, wordB)
           
        wordNetSimilarity = 0
        if self.useWordNet is True:
            wordNetSimilarity = self.wns.GetSimilarity(wordA, wordB)
            
        total = ((self.wordVectorWeight * spacySimilarity) + (self.wordNetWeight * wordNetSimilarity)) / self.totalWeight
        # print("Total: (%s * %s) + (%s * %s) = %s out of %s" % (self.wordVectorWeight, spacySimilarity, self.wordNetWeight, wordNetSimilarity, total, self.totalWeight)) # DEBUG

        return total

    # Returns the maximum similarity of a word to all words in the collection. 
    # Individual methods can use different words for maximum similarity. I.e. spacy finds A and C to have maximum similarity, and returns that value, and WordNet finds A and B to have maximum similarity, and returns that value. 
    # This means that the maximum similarity is not necessarily between just two words, but can also be between a word and multiple words in the collection.
    def GetMaxSimilarity(self, word, collection):
        total = 0

        spacySimilarity = 0
        if self.useWordVectors is True:
            spacySimilarity = self.ss.GetMaxSimilarity(word, collection)

        wordNetSimilarity = 0
        if self.useWordNet is True:
            wordNetSimilarity = self.wns.GetMaxSimilarity(word, collection)
            
        total = ((self.wordVectorWeight * spacySimilarity) + (self.wordNetWeight * wordNetSimilarity)) / self.totalWeight
        print("Total: (%s * %s) + (%s * %s) = %s out of %s" % (self.wordVectorWeight, spacySimilarity, self.wordNetWeight, wordNetSimilarity, total, self.totalWeight)) # DEBUG

        return total