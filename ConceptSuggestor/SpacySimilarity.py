class SpacySimilarity(object):
    """Establishes semantic similarity between words."""

    import spacy
    nlp = spacy.load("en_core_web_md")

    def __init__(self, concepts):
        # Convert the strings to objects that can be used by spaCy
        self.concepts = []
        for concept in concepts:
            self.concepts.append(self.nlp.vocab[concept])

    def HasSynonym(self, word, threshold):
        word = self.nlp.vocab[word]
        for groupword in self.concepts:
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

        return conceptA.similarity(conceptB)

    # Gets the maximum similarity of word to all words in the "concepts" collection.
    def GetMaxSimilarity(self, word):
        word = self.nlp.vocab[word]
        maxSimilarity = 0
        for groupword in self.concepts:
            similarity = self.GetSimilarity(word, groupword)
            if similarity > maxSimilarity:
                maxSimilarity = similarity

        return maxSimilarity