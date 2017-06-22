class SimilarityCalculator(object):
    """Calculates the similarity of two words using a variety of methods."""

    def __init__(self, settings):
        self.useSpacy = settings.UseSpacy
        if self.useSpacy is True:
            from SpacySimilarity import SpacySimilarity
            self.ss = SpacySimilarity()
            self.spacyWeight = settings.SpaCyWeight

        self.useWordNet = settings.UseWordNet
        if self.useWordNet is True:
            from WordNetSimilarity import WordNetSimilarity
            self.wns = WordNetSimilarity(settings.WordNetSimilarityMethod)
            self.wordNetWeight = settings.WordNetWeight

        self.totalSimilarityWeight = settings.TotalSimilarityWeight

        self.useSynonymity = settings.UseSynonymity
        if self.useSynonymity is True:
            from WordNetSynonyms import WordNetSynonyms
            self.wnsy = WordNetSynonyms()
            self.SimilarityThreshold = settings.SimilarityThreshold

    # Returns the similarity of two words.
    def GetSimilarity(self, wordA, wordB):
        total = 0

        spacySimilarity = 0
        if self.useSpacy is True:
            spacySimilarity = self.ss.GetSimilarity(wordA, wordB)
           
        wordNetSimilarity = 0
        if self.useWordNet is True:
            wordNetSimilarity = self.wns.GetSimilarity(wordA, wordB)
            
        total = ((self.spacyWeight * spacySimilarity) + (self.wordNetWeight * wordNetSimilarity)) / self.totalSimilarityWeight
        # print("Total: (%f * %f) + (%f * %f) = %f out of %f" % (self.wordVectorWeight, spacySimilarity, self.wordNetWeight, wordNetSimilarity, total, self.totalWeight)) # DEBUG

        if self.useSynonymity is True:
            if total >= self.SimilarityThreshold:
                if self.wnsy.IsSynonym(wordA, wordB) is True:
                    print("Synonyms found: %s, %s" % (wordA, wordB)) # DEBUG
                    return 1

        return total

    # Returns the maximum similarity of a word to all words in the collection. 
    # Individual methods can use different words for maximum similarity. I.e. spacy finds A and C to have maximum similarity, and returns that value, and WordNet finds A and B to have maximum similarity, and returns that value. 
    # This means that the maximum similarity is not necessarily between just two words, but can also be between a word and multiple words in the collection.
    def GetMaxSimilarity(self, word, collection):
        total = 0

        spacySimilarity = 0
        if self.useSpacy is True:
            spacySimilarity = self.ss.GetMaxSimilarity(word, collection)

        wordNetSimilarity = 0
        if self.useWordNet is True:
            wordNetSimilarity = self.wns.GetMaxSimilarity(word, collection)
            
        total = ((self.spacyWeight * spacySimilarity) + (self.wordNetWeight * wordNetSimilarity)) / self.totalSimilarityWeight
        print("Total: (%s * %s) + (%s * %s) = %s out of %s" % (self.spacyWeight, spacySimilarity, self.wordNetWeight, wordNetSimilarity, total, self.totalSimilarityWeight)) # DEBUG

        return total

    def ReloadSettings(self, settings):
        # Load SpaCy if necessary, and set its weight.
        self.useSpacy = settings.UseSpacy
        if self.useSpacy is True:
            if hasattr(self, "ss"):
                pass
            else:
                from SpacySimilarity import SpacySimilarity
                self.ss = SpacySimilarity()
            self.spacyWeight = settings.SpaCyWeight
        
        # Load WordNetSimilarity if necessary, and set its weight.
        self.useWordNet = settings.UseWordNet
        if self.useWordNet is True:
            if hasattr(self, "wns"):
                pass
            else:
                from WordNetSimilarity import WordNetSimilarity
                self.wns = WordNetSimilarity(settings.WordNetSimilarityMethod)
            self.wns.ReloadSettings(settings.WordNetSimilarityMethod)
            self.wordNetWeight = settings.WordNetWeight

        self.totalSimilarityWeight = settings.TotalSimilarityWeight

        # Load WordNetSynonymity if necessary, and set its threshold
        self.useSynonymity = settings.UseSynonymity
        if self.useSynonymity is True:
            if hasattr(self, "wnsy"):
                pass
            else:
                from WordNetSynonyms import WordNetSynonyms
                self.wnsy = WordNetSynonyms()
            self.SimilarityThreshold = settings.SimilarityThreshold