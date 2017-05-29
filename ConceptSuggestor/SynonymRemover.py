class SynonymRemover(object):
    """Removes synonyms using a variety of methods"""

    def __init__(self, concepts, threshold, useWordVectors = False, wordVectorWeight = 0, useThesaurus = False, thesaurusWeight = 0, useWordNet = False, wordNetWeight = 0, totalWeight = 0, totalThreshold = 0):
        self.useWordVectors = useWordVectors
        if self.useWordVectors == True:
            from SemanticSimilarity import SemanticSimilarity
            self.ss = SemanticSimilarity(concepts)
            self.wordVectorWeight = wordVectorWeight

        self.useThesaurus = useThesaurus
        if self.useThesaurus == True:
            from ThesaurusSynonyms import ThesaurusSynonyms
            self.ts = ThesaurusSynonyms()
            self.thesaurusWeight = thesaurusWeight

        self.useWordNet = useWordNet
        if self.useWordNet == True:
            from WordNetSynonyms import WordNetSynonyms
            self.wns = WordNetSynonyms()
            self.wordNetWeight = wordNetWeight

        self.totalWeight = totalWeight
        self.totalThreshold = totalThreshold

    # Returns all items in newCollection that don't have a synonym in oldCollection.
    def RemoveSynonyms(self, oldCollection, newCollection):
        noSynonyms = []
        for newItem in newCollection:
            if(not self.IsSynonym(newItem, oldCollection)):
                noSynonyms.append(newItem)

        return noSynonyms

    # Returns whether a synonym of item is in collection.
    def IsSynonym(self, item, collection):
        total = 0

        # Semantic similarity using SpaCy
        if self.useWordVectors == True:
            print("item: %s" % item)
            semanticSimilarity = self.ss.GetMaxSimilarity(item)
            semanticSimilarity *= self.wordVectorWeight
            total += semanticSimilarity

        # Checking the synonym using thesaurus
        if self.useThesaurus == True:
            thesaurus = int(self.ts.HasSynonym(item, collection))
            thesaurus *= self.thesaurusWeight
            total += thesaurus

        # Checking the synonym using WordNet
        if self.useWordNet == True:
            wordNet = int(self.wns.HasSynonym(item, collection))
            wordNet *= self.wordNetWeight
            total += wordNet

        print("Total: %s + %s + %s = %s out of %s" % (semanticSimilarity, thesaurus, wordNet, total, self.totalWeight)) # DEBUG

        total /= self.totalWeight
        if total >= self.totalThreshold:
            return True
        else:
            return False