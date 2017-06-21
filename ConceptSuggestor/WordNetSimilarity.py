from nltk.corpus import wordnet as wn

class WordNetSimilarity(object):
    """Uses WordNet to determine similarity between words."""

    def __init__(self, measure, corpus = "brown"):
        self.similarityMeasure = measure
        
        if self.similarityMeasure == "res" or self.similarityMeasure == "jcn" or self.similarityMeasure == "lin":
            LoadCorpus(corpus)

    def GetSimilarity(self, wordA, wordB):
        if wordA == wordB: # wup_similarity is coded in such a way that identical words don't necessarily return a similarity of 1, so we manually force that here.
            return 1

        wa = wn.synsets(wordA)
        wb = wn.synsets(wordB)

        similarity = 0
        if wa and wb:
            similarity = self.PerformSimilarityMeasure(wa[0], wb[0], self.similarityMeasure)

        #print("WordNet: Similarity between \"%s\" and \"%s\": %s" % (wordA, wordB, similarity)) # DEBUG
        return similarity

    def GetMaxSimilarity(self, word, collection):
        wa = wn.synsets(word)
        
        maxSimilarity = 0
        maxSimWord = "NONE" # DEBUG
        if wa:
            for wordB in collection:
                #if word == wordB: # wup_similarity is coded in such a way that identical words don't necessarily return a similarity of 1, so we manually force that here.
                    #maxSimilarity = 1
                    #maxSimWord = wordB
                    #break
                wb = wn.synsets(wordB)
                if wb:
                    similarity = self.PerformSimilarityMeasure(wa[0], wb[0], self.similarityMeasure)
                    if similarity > maxSimilarity:
                        maxSimilarity = similarity
                        maxSimWord = wordB # DEBUG

        print("WordNet: Maximum similarity %f found to word \"%s\"" % (maxSimilarity, maxSimWord)) # DEBUG
        return maxSimilarity

    def PerformSimilarityMeasure(self, synsetA, synsetB, measure):
        similarity = 0

        # Path-based measures
        if measure == "path": # shortest path is-a (hypernym/hyponym) taxonomy
            similarity = synsetA.path_similarity(synsetB)
        elif measure == "lch": # Leacock-Chodorow
            similarity = synsetA.lch_similarity(synsetB)
        elif measure == "wup": # Wu-Palmer
            similarity = synsetA.wup_similarity(synsetB)

        # IC-based measures
        elif measure == "res": # Resnik
            similarity = synsetA.res_similarity(synsetB, self.ic)
        elif measure == "jcn": # Jiang-Conrath
            similarity = synsetA.jcn_similarity(synsetB, self.ic)
        elif measure == "lin": # Lin
            similarity = synsetA.lin_similarity(synsetB, self.ic)

        return similarity

    def ReloadSettings(self, measure):
        self.similarityMeasure = measure
        if measure == "res" or measure == "jcn" or measure == "lin":
            if hasattr(self, 'ic'):
                pass
            else:
                LoadCorpus()

    def LoadCorpus(self, corpus = "brown"):
        print("Loading \"%s\" Information Content corpus..." % corpus)
        from nltk.corpus import wordnet_ic as wnic 
        # Loads Information Content used for similarity measuring.
        if corpus == "semcor":
            self.ic = wnic.ic("ic-semcor.dat") 
        elif corpus == "brown":
            self.ic = wnic.ic("ic-brown.dat")