class CompoundHandler(object):
    """Handles compound terms."""

    def __init__(self, threshold, useWordVectors = False, wordVectorWeight = 0, useThesaurus = False, thesaurusWeight = 0, useWordNet = False, wordNetWeight = 0, totalWeight = 0, totalThreshold = 0):
        from SimilarityCalculator import SimilarityCalculator
        self.sc = SimilarityCalculator(threshold, 
                                       useWordVectors = useWordVectors, wordVectorWeight = wordVectorWeight, 
                                       useThesaurus = useThesaurus, thesaurusWeight = thesaurusWeight, 
                                       useWordNet = useWordNet, wordNetWeight = wordNetWeight, 
                                       totalWeight = totalWeight)

    # NOT YET IMPLEMENTED
    def GetSimilarity(self, compoundA, compoundB):
        return 0.0