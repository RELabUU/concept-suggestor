class SynonymRemover(object):
    """Removes synonyms using a variety of methods"""

    def __init__(self, concepts, useWordVectors = False, wordVectorWeight = 0, useWordNet = False, wordNetWeight = 0, totalWeight = 0, totalThreshold = 0):
        from SimilarityCalculator import SimilarityCalculator
        self.sc = SimilarityCalculator(useWordVectors = useWordVectors, wordVectorWeight = wordVectorWeight,
                                       useWordNet = useWordNet, wordNetWeight = wordNetWeight,
                                       totalWeight = totalWeight)

        self.totalThreshold = totalThreshold

    # Returns all items in newCollection that don't have a synonym in oldCollection.
    def RemoveSynonyms(self, oldCollection, newCollection):
        noSynonyms = []
        for newItem in newCollection:
            print("Comparing %s to collection:" % newItem) # DEBUG
            if(not self.IsSynonym(newItem, oldCollection)):
                noSynonyms.append(newItem)

        return noSynonyms

    # Returns whether a synonym of item is in collection.
    def IsSynonym(self, item, collection):
        similarity = self.sc.GetMaxSimilarity(item, collection)

        if similarity >= self.totalThreshold:
            return True
        else:
            return False