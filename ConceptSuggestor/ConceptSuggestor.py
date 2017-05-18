# The concepts that are already in the model.
concepts = ["Aircraft", "Flight", "Gate", "Ticket", "Airspace", "Pilot", "Security", "Route"]
print("Concepts already in the model: %s" % concepts)


def IsValidChoice(choice):
    if(choice=="a" or choice=="b"):
        return True
    else:
        return False

def GetProgramMode():
    print("These are your options:")
    print("a - check similarity using word vectors")
    print("b - check whether a synonym exists using thesaurus.com")

    # Get the program mode from the user and ensure it's valid.
    choice = input("Please tell me what to do (type a letter): ").lower()
    if(IsValidChoice(choice)):
        return choice
    else:
        print("I could not understand that option. Please try again.")
        return GetProgramMode()

    return choice

choice = GetProgramMode()
new = input("Enter a concept to be checked for similarity: ")

if(choice == "a"):
    from SynonymRemover import SynonymRemover
    print("Result of semantic similarity: ")
    sr = SynonymRemover(concepts)
    print(sr.HasSynonym(new))

elif(choice=="b"):
    from DictionarySynonyms import DictionarySynonyms
    print("Result of Thesaurus.com synonyms: ")
    ds = DictionarySynonyms()
    print(ds.HasSynonym(concepts, new))

else:
    print("Invalid mode. Aborting.")