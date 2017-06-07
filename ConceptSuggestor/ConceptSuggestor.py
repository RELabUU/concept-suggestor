COMMITFILE = "commit_example2.json" # Example commit to load
CONCEPTSFILE = "concepts_example.json" # Example concepts already in the model
OUTFILE = "suggestions_example.json" # Example file to send after request
AIRMFILE = "AIRM/EA4A02.informationmodel.xml" # AIRM information model

WORDVECTOR_THRESHOLD = 0.9
TOTAL_THRESHOLD = 0.8

USEWORDVECTORS = True
USETHESAURUS = True
USEWORDNET = True

WORDVECTOR_WEIGHT = 0.5
THESAURUS_WEIGHT = 0.5
WORDNET_WEIGHT = 0.5
TOTAL_WEIGHT = WORDVECTOR_WEIGHT + THESAURUS_WEIGHT + WORDNET_WEIGHT

collections = { "one": "concepts_example.json",
                "two": "concepts_example2.json" }

def IsValidChoice(choice):
    if(choice=="a" or choice=="b" or choice=="c" or choice=="d" or choice=="e" or choice=="f" or choice=="g" or choice=="h"):
        return True
    else:
        return False

def GetProgramMode():
    print("These are your options:")
    print("a - The complete parameterized package. Loads new concepts from external JSON file, removes synonyms, and writes that to an external JSON file.")
    print("b - Check similarity using word vectors.")
    print("c - Check whether a synonym exists using thesaurus.com.")
    print("d - Check similarity using WordNet.")
    print("e - Open a JSON file.")
    print("f - Open the AIRM file.")
    print("g - Opens multiple collections and finds the ratio of occurence of a word.")
    print("h - Compares two possibly compound terms and returns the similarity between them.")

    # Get the program mode from the user and ensure it's valid.
    choice = input("Please tell me what to do (type a letter): ").lower()
    if IsValidChoice(choice):
        return choice
    else:
        print("I could not understand that option. Please try again.")
        return GetProgramMode()

    return choice

def Main():
    from JsonParser import JsonParser
    jp = JsonParser()
    
    # The concepts that are already in the model.
    concepts = jp.LoadFile(CONCEPTSFILE)
    print("Concepts already in the model: %s" % concepts)

    choice = GetProgramMode()
    if choice == "b" or choice == "c" or choice == "d" or choice == "g":
        new = input("Enter a concept you want to check whether we have a synonym for (i.e. Aeroplane): ")

    if choice == "a":
        from SynonymRemover import SynonymRemover
        sr = SynonymRemover(concepts, TOTAL_THRESHOLD, 
                            useWordVectors = USEWORDVECTORS, wordVectorWeight = WORDVECTOR_WEIGHT,
                            useThesaurus = USETHESAURUS, thesaurusWeight = THESAURUS_WEIGHT, 
                            useWordNet = USEWORDNET, wordNetWeight = WORDNET_WEIGHT,
                            totalWeight = TOTAL_WEIGHT, totalThreshold = TOTAL_THRESHOLD)
        
        from JsonParser import JsonParser
        jp = JsonParser()
        newConcepts = jp.LoadCommit(COMMITFILE)

        newConcepts = sr.RemoveSynonyms(concepts, newConcepts)

        print("New concepts: %s" % newConcepts)
        jp.MakeFile(newConcepts, OUTFILE)

    elif choice == "b":
        from SpacySimilarity import SpacySimilarity
        print("Result of semantic similarity: ")
        ss = SpacySimilarity(concepts)
        print(ss.HasSynonym(new, WORDVECTOR_THRESHOLD))

    elif choice=="c":
        from ThesaurusSynonyms import ThesaurusSynonyms
        print("Result of Thesaurus.com synonyms: ")
        ds = ThesaurusSynonyms()
        print(ds.HasSynonym(new, concepts))

    elif choice=="d":
        from WordNetSimilarity import WordNetSimilarity
        print("Result of WordNet similarity: ")
        wns = WordNetSimilarity()
        print(wns.GetMaxSimilarity(new, concepts))

    elif choice=="e":
        from JsonParser import JsonParser
        print("Result of JsonParser: ")
        jp = JsonParser()
        data = jp.LoadCommit(COMMITFILE)
        print(data)
        jp.MakeFile(data, OUTFILE)

    elif choice=="f":
        from XmlParser import XmlParser
        print("Result of XmlParser: ")
        xp = XmlParser()
        data = xp.LoadFile(AIRMFILE)
        print(data)

    elif choice=="g":
        from CollectionManager import CollectionManager
        print("Result of CollectionManager: ")
        cm = CollectionManager()
        cm.LoadCollections(collections)
        print(cm.FrequencyOfWord(new))

    elif choice=="h":
        from CompoundHandler import CompoundHandler
        print("Result of CompoundHandler: ")
        ch = CompoundHandler(TOTAL_THRESHOLD,
                             useWordVectors = USEWORDVECTORS, wordVectorWeight = WORDVECTOR_WEIGHT,
                             useThesaurus = USETHESAURUS, thesaurusWeight = THESAURUS_WEIGHT,
                             useWordNet = USEWORDNET, wordNetWeight = WORDNET_WEIGHT,
                             totalWeight = TOTAL_WEIGHT, totalThreshold = TOTAL_THRESHOLD)
        compoundA = input("Enter the first possibly compound term: ")
        compoundB = input("Enter the second possibly compound term: ")
        print(ch.GetSimilarity(compoundA, compoundB))

    else:
        print("Invalid mode. Aborting.")

Main()