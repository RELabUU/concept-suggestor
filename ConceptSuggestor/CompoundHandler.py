class CompoundHandler(object):
    """Handles compound terms."""

    # ALPHA + BETA = 1     ALPHA >= BETA
    ALPHA = 0.67
    BETA = 0.33

    # GAMMA + DELTA + 2*EPSILON = 1     GAMMA >= DELTA >= 2*EPSILON
    GAMMA = 0.5
    DELTA = 0.3
    EPSILON = 0.1

    def __init__(self, threshold, useWordVectors = False, wordVectorWeight = 0, useWordNet = False, wordNetWeight = 0, totalWeight = 0, totalThreshold = 0):
        from SimilarityCalculator import SimilarityCalculator
        self.sc = SimilarityCalculator(threshold, 
                                       useWordVectors = useWordVectors, wordVectorWeight = wordVectorWeight, 
                                       useWordNet = useWordNet, wordNetWeight = wordNetWeight, 
                                       totalWeight = totalWeight)

    def GetSimilarity(self, compoundA, compoundB):
        wordsA = compoundA.split()
        wordsB = compoundB.split()

        if len(wordsA) > 2 or len(wordsB) > 2:
            print("We don't support compounds larger than two words yet.")
            return -1.0
        if len(wordsA) == 0 or len(wordsB) == 0:
            print("One of the compounds is empty.")
            return -1.0

        compoundAisCompound = len(wordsA) > 1
        compoundBisCompound = len(wordsB) > 1

        # Level - Altitude
        if compoundAisCompound is not True and compoundBisCompound is not True:
            print("Comparing %s to %s:" % (wordsA[0], wordsB[0])) # DEBUG
            similarity = self.sc.GetSimilarity(wordsA[0], wordsB[0])
            print("Similarity: %s <> %s = %s" % (wordsA[0], wordsB[0], similarity)) # DEBUG

        # Flight Level - Altitude
        elif compoundAisCompound is True and compoundBisCompound is not True:
            print("Comparing %s to %s:" % (wordsA[1], wordsB[0])) # DEBUG
            similarityA = self.sc.GetSimilarity(wordsA[1], wordsB[0]) # Level - Altitude
            print("similarityA: %s <> %s = %s\n" % (wordsA[1], wordsB[0], similarityA)) # DEBUG

            print("Comparing %s to %s:" % (wordsA[0], wordsB[0])) # DEBUG
            similarityB = self.sc.GetSimilarity(wordsA[0], wordsB[0]) # Flight - Altitude
            print("similarityB: %s <> %s = %s\n" % (wordsA[0], wordsB[0], similarityB)) # DEBUG

            similarity = (self.ALPHA * similarityA + 
                          self.BETA * similarityB)
            print("Similarity: %s * %s + %s * %s = %s" % (self.ALPHA, similarityA, self.BETA, similarityB, similarity)) # DEBUG

        # Level - Flight Altitude
        elif compoundAisCompound is not True and compoundBisCompound is True:
            print("Comparing %s to %s:" % (wordsA[0], wordsB[1])) # DEBUG
            similarityA = self.sc.GetSimilarity(wordsA[0], wordsB[1]) # Level - Altitude
            print("similarityA: %s <> %s = %s\n" % (wordsA[0], wordsB[1], similarityA)) # DEBUG

            print("Comparing %s to %s:" % (wordsA[0], wordsB[0])) # DEBUG
            similarityB = self.sc.GetSimilarity(wordsA[0], wordsB[0]) # Level - Flight
            print("similarityB: %s <> %s = %s\n" % (wordsA[0], wordsB[0], similarityB)) # DEBUG

            similarity = (self.ALPHA * similarityA + 
                          self.BETA * similarityB)
            print("Similarity: %s * %s + %s * %s = %s" % (self.ALPHA, similarityA, self.BETA, similarityB, similarity)) # DEBUG

        # Flight Level - Flight Altitude
        else:
            print("Comparing %s to %s:" % (wordsA[1], wordsB[1])) # DEBUG
            similarityC = self.sc.GetSimilarity(wordsA[1], wordsB[1]) # Level - Altitude
            print("similarityC: %s <> %s = %s\n" % (wordsA[1], wordsB[1], similarityC)) # DEBUG

            print("Comparing %s to %s:" % (wordsA[0], wordsB[0])) # DEBUG
            similarityD = self.sc.GetSimilarity(wordsA[0], wordsA[0]) # Flight - Flight
            print("similarityD: %s <> %s = %s\n" % (wordsA[0], wordsB[0], similarityD)) # DEBUG

            print("Comparing %s to %s:" % (wordsA[0], wordsB[1])) # DEBUG
            similarityEa = self.sc.GetSimilarity(wordsA[0], wordsB[1]) # Flight - Altitude
            print("similarityEa: %s <> %s = %s\n" % (wordsA[0], wordsB[1], similarityEa)) # DEBUG

            print("Comparing %s to %s:" % (wordsA[1], wordsB[0])) # DEBUG
            similarityEb = self.sc.GetSimilarity(wordsA[1], wordsB[0]) # Level - Flight
            print("similarityEb: %s <> %s = %s\n" % (wordsA[1], wordsB[0], similarityEb)) # DEBUG

            similarity = (self.GAMMA * similarityC + 
                          self.DELTA * similarityD + 
                          self.EPSILON * similarityEa + 
                          self.EPSILON * similarityEb)
            print("Similarity: (%s * %s) + (%s * %s) + (%s * %s) + (%s * %s) = %s" % (self.GAMMA, similarityC, self.DELTA, similarityD, self.EPSILON, similarityEa, self.EPSILON, similarityEb, similarity)) # DEBUG

        return similarity