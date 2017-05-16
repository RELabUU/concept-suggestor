from SynonymRemover import SynonymRemover

# The concepts that are already in the model.
concepts = ["Airplane", "Flight", "Gate", "Ticket", "Aerospace", "Pilot"]

sr = SynonymRemover(concepts)
new = input("Enter a concept to be checked for similarity: ")
print(sr.HasSynonym(new))