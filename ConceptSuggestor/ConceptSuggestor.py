from SynonymRemover import SynonymRemover
from DictionarySynonyms import DictionarySynonyms

# The concepts that are already in the model.
concepts = ["Aircraft", "Flight", "Gate", "Ticket", "Airspace", "Pilot", "Security", "Route"]

print("Concepts already in the model: %s" % concepts)
new = input("Enter a concept to be checked for similarity: ")

print("Result of semantic similarity: ")
sr = SynonymRemover(concepts)
print(sr.HasSynonym(new))

print("Result of Thesaurus.com synonyms: ")
ds = DictionarySynonyms()
print(ds.HasSynonym(concepts, new))