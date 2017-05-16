import spacy
nlp = spacy.load("en_core_web_md")

class SynonymRemover(object):
    """Removes synonyms"""
    THRESHOLD = 0.9

    def __init__(self, concepts):
        # Convert the strings to objects that can be used by spaCy
        self.concepts = []
        for concept in concepts:
            self.concepts.append(nlp.vocab[concept])

    def HasSynonym(self, word):
        word = nlp.vocab[word]
        for groupword in self.concepts:
            if(self.IsSynonym(groupword, word)):
                return True
        # We get here if no synonyms are found
        return False

    def IsSynonym(self, wordA, wordB):
        similarity = wordA.similarity(wordB)
        print("%s - %s: %s" % (wordA.norm_, wordB.norm_, similarity))
        if(similarity >= self.THRESHOLD):
            return True
        else:
            return False