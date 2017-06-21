class CompoundHandler(object):
    """Handles compound terms."""

    import Settings

    def __init__(self, settings):
        self.s = settings

        from SimilarityCalculator import SimilarityCalculator
        self.sc = SimilarityCalculator(self.s)

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
            # print("Comparing %s to %s:" % (wordsA[0], wordsB[0])) # DEBUG
            similarity = self.sc.GetSimilarity(wordsA[0], wordsB[0])
            print("Similarity: %s <> %s = %f" % (wordsA[0], wordsB[0], similarity)) # DEBUG

        # Flight Level - Altitude
        elif compoundAisCompound is True and compoundBisCompound is not True:
            # print("Comparing %s to %s:" % (wordsA[1], wordsB[0])) # DEBUG
            similarityA = self.sc.GetSimilarity(wordsA[1], wordsB[0]) # Level - Altitude
            print("similarityA: %s <> %s = %f" % (wordsA[1], wordsB[0], similarityA)) # DEBUG

            # print("Comparing %s to %s:" % (wordsA[0], wordsB[0])) # DEBUG
            similarityB = self.sc.GetSimilarity(wordsA[0], wordsB[0]) # Flight - Altitude
            print("similarityB: %s <> %s = %f" % (wordsA[0], wordsB[0], similarityB)) # DEBUG

            similarity = (self.s._Setting("alpha") * similarityA + 
                          self.s._Setting("beta") * similarityB)
            print("Similarity: %f * %f + %f * %f = %f" % (self.s.Alpha(), similarityA, 
                                                          self.s.Beta(), similarityB, 
                                                          similarity)) # DEBUG

        # Level - Flight Altitude
        elif compoundAisCompound is not True and compoundBisCompound is True:
            # print("Comparing %s to %s:" % (wordsA[0], wordsB[1])) # DEBUG
            similarityA = self.sc.GetSimilarity(wordsA[0], wordsB[1]) # Level - Altitude
            print("similarityA: %s <> %s = %f" % (wordsA[0], wordsB[1], similarityA)) # DEBUG

            # print("Comparing %s to %s:" % (wordsA[0], wordsB[0])) # DEBUG
            similarityB = self.sc.GetSimilarity(wordsA[0], wordsB[0]) # Level - Flight
            print("similarityB: %s <> %s = %f" % (wordsA[0], wordsB[0], similarityB)) # DEBUG

            similarity = (self.s._Setting("alpha") * similarityA + 
                          self.s._Setting("beta") * similarityB)
            print("Similarity: %f * %f + %f * %f = %f" % (self.s.Alpha(), similarityA, 
                                                          self.s.Alpha(), similarityB, 
                                                          similarity)) # DEBUG

        # Flight Level - Flight Altitude
        else:
            # print("Comparing %s to %s:" % (wordsA[1], wordsB[1])) # DEBUG
            similarityC = self.sc.GetSimilarity(wordsA[1], wordsB[1]) # Level - Altitude
            print("similarityC: %s <> %s = %f" % (wordsA[1], wordsB[1], similarityC)) # DEBUG

            # print("Comparing %s to %s:" % (wordsA[0], wordsB[0])) # DEBUG
            similarityD = self.sc.GetSimilarity(wordsA[0], wordsB[0]) # Flight - Flight
            print("similarityD: %s <> %s = %f" % (wordsA[0], wordsB[0], similarityD)) # DEBUG

            # print("Comparing %s to %s:" % (wordsA[0], wordsB[1])) # DEBUG
            similarityEa = self.sc.GetSimilarity(wordsA[0], wordsB[1]) # Flight - Altitude
            print("similarityEa: %s <> %s = %f" % (wordsA[0], wordsB[1], similarityEa)) # DEBUG

            # print("Comparing %s to %s:" % (wordsA[1], wordsB[0])) # DEBUG
            similarityEb = self.sc.GetSimilarity(wordsA[1], wordsB[0]) # Level - Flight
            print("similarityEb: %s <> %s = %f" % (wordsA[1], wordsB[0], similarityEb)) # DEBUG

            similarity = (self.s._Setting("gamma") * similarityC + 
                          self.s._Setting("delta") * similarityD + 
                          self.s._Setting("epsilon") * similarityEa + 
                          self.s._Setting("epsilon") * similarityEb)
            print("Similarity: (%f * %f) + (%f * %f) + (%f * %f) + (%f * %f) = %f" % (self.s.Gamma(), similarityC, 
                                                                                      self.s.Delta(), similarityD, 
                                                                                      self.s.Epsilon(), similarityEa, 
                                                                                      self.s.Epsilon(), similarityEb, 
                                                                                      similarity)) # DEBUG

        return similarity