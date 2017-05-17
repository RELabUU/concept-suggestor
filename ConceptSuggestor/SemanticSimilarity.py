class SemanticSimilarity(object):
    """Establishes semantic similarity between words."""

    def __init__(self, nlp):
        self.nlp = nlp

    # Gets the vector of a string, or returns the object if it's already a vector.
    def StringToVector(self, object):
        if(type(object) == str):
            return self.nlp.vocab[object]
        else:
            return object

    # Gets the similarity of two concepts (can be strings or vectors)
    def GetSimilarity(self, conceptA, conceptB):
        # Ensure inputs are vectors and not strings
        conceptA = self.StringToVector(conceptA)
        conceptB = self.StringToVector(conceptB)

        return conceptA.similarity(conceptB)