import spacy

class SpacySimilarity(object):
    """Establishes semantic similarity between words."""

    PACKAGE = "en_core_web_md"

    def __init__(self, collection = []):
        # Convert the strings to objects that can be used by spaCy
        print("Loading SpaCy's %s model..." % self.PACKAGE) # DEBUG
        self.nlp = spacy.load(self.PACKAGE)

        # If a collection is specified to load, load it so that loading is not redundantly done elsewhere.
        self.collection = []
        for word in collection:
            self.collection.append(self.nlp.vocab[word])

    def HasSynonym(self, word, threshold, collection = [],):
        word = self.nlp.vocab[word]

        # If a collection has been loaded previously, and none is passed to this method, use the previously loaded collection of words
        if self.collection != [] and collection == []:
            newcollection = self.collection
        else:
            newcollection = []
            for groupword in collection:
                newcollection.append(self.nlp.vocab[groupword])

        for groupword in newcollection:
            if self.IsSynonym(groupword, word, threshold):
                return True
        # We get here if no synonyms are found
        return False

    def IsSynonym(self, wordA, wordB, threshold):
        similarity = self.GetSimilarity(wordA, wordB)
        print("%s - %s: %s" % (wordA.norm_, wordB.norm_, similarity)) # DEBUG
        if similarity >= threshold:
            return True
        else:
            return False

    # Gets the vector of a string, or returns the object if it's already a vector.
    def StringToVector(self, object):
        if type(object) == str:
            return self.nlp.vocab[object]
        else:
            return object

    # Gets the similarity of two concepts (can be strings or vectors)
    def GetSimilarity(self, conceptA, conceptB):
        # Ensure inputs are vectors and not strings
        conceptA = self.StringToVector(conceptA)
        conceptB = self.StringToVector(conceptB)

        result = conceptA.similarity(conceptB)
        print("SpaCy: Similarity between \"%s\" and \"%s\": %s" % (conceptA.lower_, conceptB.lower_, result)) # DEBUG
        return result

    # Gets the maximum similarity of word to all words in the "concepts" collection.
    def GetMaxSimilarity(self, word, collection = []):
        word = self.nlp.vocab[word]
        maxSimilarity = 0
        maxSimWord = "NONE" # DEBUG

        if self.collection != [] and collection == []:
            newcollection = self.collection
        else:
            newcollection = []
            for groupword in collection:
                newcollection.append(self.nlp.vocab[groupword])

        for groupword in newcollection:
            similarity = self.GetSimilarity(word, groupword)
            if similarity > maxSimilarity:
                maxSimilarity = similarity
                maxSimWord = groupword.lower_ # DEBUG

        print("SpaCy: Maximum similarity %s found to word \"%s\"" % (maxSimilarity, maxSimWord)) # DEBUG
        return maxSimilarity