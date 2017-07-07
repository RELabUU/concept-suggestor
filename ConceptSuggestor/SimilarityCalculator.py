class SimilarityCalculator(object):
    """Calculates the similarity of two words using a variety of methods."""

    def __init__(self, settings, loadAll = False):
        self.s = settings

        if self.s.UseSpacy is True or loadAll is True:
            from SpacySimilarity import SpacySimilarity
            self.ss = SpacySimilarity()

        if self.s.UseWordNet is True or loadAll is True:
            from WordNetSimilarity import WordNetSimilarity
            self.wns = WordNetSimilarity(settings.WordNetSimilarityMethod)

        if self.s.UseSynonymity is True or loadAll is True:
            from WordNetSynonyms import WordNetSynonyms
            self.wnsy = WordNetSynonyms()

    # Returns the similarity of two words.
    def GetSimilarity(self, wordA, wordB):
        total = 0

        spacySimilarity = 0
        if self.s.UseSpacy == True:
            spacySimilarity = self.ss.GetSimilarity(wordA, wordB)
           
        wordNetSimilarity = 0
        if self.s.UseWordNet == True:
            wordNetSimilarity = self.wns.GetSimilarity(wordA, wordB)
            
        total = ((self.s.SpaCyWeight * spacySimilarity) + (self.s.WordNetWeight * wordNetSimilarity)) / self.s.TotalSimilarityWeight
        # print("sc: Total: (%f * %f) + (%f * %f) = %f out of %f" % (self.s.SpaCyWeight, spacySimilarity, self.s.WordNetWeight, wordNetSimilarity, total, self.s.TotalSimilarityWeight)) # DEBUG

        if self.s.UseSynonymity is True:
            if total >= self.s.SimilarityThreshold:
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
        if self.s.UseSpacy is True:
            spacySimilarity = self.ss.GetMaxSimilarity(word, collection)

        wordNetSimilarity = 0
        if self.s.UseWordNet is True:
            wordNetSimilarity = self.wns.GetMaxSimilarity(word, collection)
            
        total = ((self.s.SpaCyWeight * spacySimilarity) + (self.s.WordNetWeight * wordNetSimilarity)) / self.s.TotalSimilarityWeight
        print("Total: (%s * %s) + (%s * %s) = %s out of %s" % (self.s.SpaCyWeight, spacySimilarity, self.s.WordNetWeight, wordNetSimilarity, total, self.s.TotalSimilarityWeight)) # DEBUG

        return total

    def ReloadSettings(self, settings):
        # Load SpaCy if necessary, and set its weight.
        if self.s.UseSpacy is True:
            if hasattr(self, "ss"):
                pass
            else:
                from SpacySimilarity import SpacySimilarity
                self.ss = SpacySimilarity()
        
        # Load WordNetSimilarity if necessary, and set its weight.
        if self.s.UseWordNet is True:
            if hasattr(self, "wns"):
                pass
            else:
                from WordNetSimilarity import WordNetSimilarity
                self.wns = WordNetSimilarity(settings.WordNetSimilarityMethod)
            self.wns.ReloadSettings(settings.WordNetSimilarityMethod)

        # Load WordNetSynonymity if necessary, and set its threshold
        if self.s.UseSynonymity is True:
            if hasattr(self, "wnsy"):
                pass
            else:
                from WordNetSynonyms import WordNetSynonyms
                self.wnsy = WordNetSynonyms()