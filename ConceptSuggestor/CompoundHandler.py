class CompoundHandler(object):
    """Handles compound terms."""

    import Settings

    def __init__(self, settings, loadAll = False):
        self.s = settings

        from SimilarityCalculator import SimilarityCalculator
        self.sc = SimilarityCalculator(self.s, loadAll = loadAll)

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
            # print("Comparing %s to %s:" % (wordsA[0], wordsB[0])) # DEBUG
            similarityA = self.sc.GetSimilarity(wordsA[0], wordsB[0]) # Flight - Altitude
            print("similarityA: %s <> %s = %f" % (wordsA[0], wordsB[0], similarityA)) # DEBUG

            # print("Comparing %s to %s:" % (wordsA[1], wordsB[0])) # DEBUG
            similarityB = self.sc.GetSimilarity(wordsA[1], wordsB[0]) # Level - Altitude
            print("similarityB: %s <> %s = %f" % (wordsA[1], wordsB[0], similarityB)) # DEBUG

            similarity = (self.s.Alpha * similarityA + 
                          self.s.Beta * similarityB)
            print("Similarity: %f * %f + %f * %f = %f" % (self.s.Alpha, similarityA, 
                                                          self.s.Beta, similarityB, 
                                                          similarity)) # DEBUG

        # Level - Flight Altitude
        elif compoundAisCompound is not True and compoundBisCompound is True:
            # print("Comparing %s to %s:" % (wordsA[0], wordsB[0])) # DEBUG
            similarityA = self.sc.GetSimilarity(wordsA[0], wordsB[0]) # Level - Flight
            print("similarityA: %s <> %s = %f" % (wordsA[0], wordsB[0], similarityA)) # DEBUG

            # print("Comparing %s to %s:" % (wordsA[0], wordsB[1])) # DEBUG
            similarityB = self.sc.GetSimilarity(wordsA[0], wordsB[1]) # Level - Altitude
            print("similarityB: %s <> %s = %f" % (wordsA[0], wordsB[1], similarityB)) # DEBUG

            similarity = (self.s.Alpha * similarityA + 
                          self.s.Beta * similarityB)
            print("Similarity: %f * %f + %f * %f = %f" % (self.s.Alpha, similarityA, 
                                                          self.s.Alpha, similarityB, 
                                                          similarity)) # DEBUG

        # Flight Level - Flight Altitude
        else:
            # print("Comparing %s to %s:" % (wordsA[0], wordsB[0])) # DEBUG
            similarityC = self.sc.GetSimilarity(wordsA[0], wordsB[0]) # Flight - Flight
            print("similarityC: %s <> %s = %f" % (wordsA[0], wordsB[0], similarityC)) # DEBUG

            # print("Comparing %s to %s:" % (wordsA[1], wordsB[1])) # DEBUG
            similarityD = self.sc.GetSimilarity(wordsA[1], wordsB[1]) # Level - Altitude
            print("similarityD: %s <> %s = %f" % (wordsA[1], wordsB[1], similarityD)) # DEBUG

            # print("Comparing %s to %s:" % (wordsA[0], wordsB[1])) # DEBUG
            similarityEa = self.sc.GetSimilarity(wordsA[0], wordsB[1]) # Flight - Altitude
            print("similarityEa: %s <> %s = %f" % (wordsA[0], wordsB[1], similarityEa)) # DEBUG

            # print("Comparing %s to %s:" % (wordsA[1], wordsB[0])) # DEBUG
            similarityEb = self.sc.GetSimilarity(wordsA[1], wordsB[0]) # Level - Flight
            print("similarityEb: %s <> %s = %f" % (wordsA[1], wordsB[0], similarityEb)) # DEBUG

            similarity = (self.s.Gamma * similarityC + 
                          self.s.Delta * similarityD + 
                          self.s.Epsilon * similarityEa + 
                          self.s.Epsilon * similarityEb)
            print("Similarity: (%f * %f) + (%f * %f) + (%f * %f) + (%f * %f) = %f" % (self.s.Gamma, similarityC, 
                                                                                      self.s.Delta, similarityD, 
                                                                                      self.s.Epsilon, similarityEa, 
                                                                                      self.s.Epsilon, similarityEb, 
                                                                                      similarity)) # DEBUG

        return similarity

    def ReloadSettings(self, settings):
        self.s = settings

        self.sc.ReloadSettings(settings)