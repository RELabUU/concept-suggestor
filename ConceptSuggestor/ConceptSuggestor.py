# The concepts that are already in the model.
concepts = ["Airplane", "Flight", "Gate", "Ticket", "Airspace", "Pilot", "Security", "Route"]
print("Concepts already in the model: %s" % concepts)


def IsValidChoice(choice):
    if(choice=="a" or choice=="b" or choice=="c" or choice=="d"):
        return True
    else:
        return False

def GetProgramMode():
    print("These are your options:")
    print("a - Check similarity using word vectors")
    print("b - Check whether a synonym exists using thesaurus.com")
    print("c - Check whether a synonym exists using WordNet")
    print("d - Open a JSON file")

    # Get the program mode from the user and ensure it's valid.
    choice = input("Please tell me what to do (type a letter): ").lower()
    if(IsValidChoice(choice)):
        return choice
    else:
        print("I could not understand that option. Please try again.")
        return GetProgramMode()

    return choice

choice = GetProgramMode()
if(choice != "d"):
    new = input("Enter a concept you want to check whether we have a synonym for (i.e. Aeroplane): ")

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

elif(choice=="c"):
    from WordNetSynonyms import WordNetSynonyms
    print("Result of WordNet synonyms: ")
    wns = WordNetSynonyms()
    print(wns.HasSynonym(concepts, new))

elif(choice=="d"):
    from JsonParser import JsonParser
    print("Result of JsonParser: ")
    jp = JsonParser()
else:
    print("Invalid mode. Aborting.")