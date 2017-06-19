from Settings import Settings
s = Settings()

COMMITFILE = "commit_example2.json" # Example commit to load
CONCEPTSFILE = "concepts_example.json" # Example concepts already in the model
OUTFILE = "suggestions_example.json" # Example file to send after request
AIRMFILE = "AIRM/EA4A02.informationmodel.xml" # AIRM information model
COMPOUNDSFILE = "compound_concepts.json" # File containing compound words and their human-estimated similarity.

USEWORDVECTORS = True
USEWORDNET = True

WORDVECTOR_WEIGHT = 0.5
WORDNET_WEIGHT = 0.5
TOTAL_WEIGHT = WORDVECTOR_WEIGHT + WORDNET_WEIGHT

collections = { "one": "concepts_example.json",
                "two": "concepts_example2.json" }

def GetProgramMode():
    print("These are your options:")
    print("a - Example Functionality. Loads new concepts from external JSON file, removes synonyms, and writes that to an external JSON file.")
    print("b - Compare similarity of a word to loaded concepts using SpaCy's word vectors.")
    print("c - Compare similarity of a word to loaded concepts using WordNet's similarity function.")
    print("d - Open a JSON file.")
    print("e - Open the AIRM file.")
    print("f - Opens multiple collections and finds the ratio of occurence of a word.")
    print("g - Compares two possibly compound terms and returns the similarity between them.")
    print("h - Tests compound terms found in compound_concepts.json for similarity.")

    # Get the program mode from the user and ensure it's valid.
    choice = input("Please tell me what to do (type a letter): ").lower()
    if IsValidChoice(choice):
        return choice
    else:
        print("I could not understand that option. Please try again.")
        return GetProgramMode()

    return choice

def Main():
    choice = GetProgramMode()

    if choice == "a":
        TestCompletePackage(LoadConcepts())
    elif choice == "b":
        TestSpacySimilarity(LoadConcepts())
    elif choice == "c":
        TestWordNetSimilarity(LoadConcepts())
    elif choice == "d":
        TestJsonParser()
    elif choice == "e":
        TestXmlParser()
    elif choice == "f":
        TestCollectionManager()
    elif choice == "g":
        TestCompoundHandler()
    elif choice == "h":
        TestExternalCompounds()
    else:
        print("Invalid mode. Aborting.")

def LoadConcepts():
    from JsonParser import JsonParser

    jp = JsonParser()

    return jp.LoadFile(CONCEPTSFILE, debug = True) # DEBUG - Not the entire line, only the "debug = True" part.

def TestCompletePackage(existingConcepts):
    from SynonymRemover import SynonymRemover
    sr = SynonymRemover(existingConcepts, 
                        useWordVectors = USEWORDVECTORS, wordVectorWeight = WORDVECTOR_WEIGHT,
                        useWordNet = USEWORDNET, wordNetWeight = WORDNET_WEIGHT,
                        totalWeight = TOTAL_WEIGHT, totalThreshold = TOTAL_THRESHOLD)
        
    from JsonParser import JsonParser
    jp = JsonParser()
    newConcepts = jp.LoadCommit(COMMITFILE)

    newConcepts = sr.RemoveSynonyms(existingConcepts, newConcepts)

    print("New concepts: %s" % newConcepts)
    jp.MakeFile(newConcepts, OUTFILE)

def TestSpacySimilarity(existingConcepts):
    from SpacySimilarity import SpacySimilarity
    ss = SpacySimilarity(existingConcepts)
    while True:
        ss.GetMaxSimilarity(GetInputWord())
        if not TryAgain():
            break

def TestWordNetSimilarity(existingConcepts):
    from WordNetSimilarity import WordNetSimilarity
    wns = WordNetSimilarity()
    while True:
        wns.GetMaxSimilarity(GetInputWord(), existingConcepts)
        if not TryAgain():
            break

def TestJsonParser():
    from JsonParser import JsonParser
    jp = JsonParser()
    data = jp.LoadCommit(COMMITFILE)
    jp.MakeFile(data, OUTFILE)
    print("Concepts written to %s." % OUTFILE)

def TestXmlParser():
    from XmlParser import XmlParser
    xp = XmlParser()
    data = xp.LoadFile(AIRMFILE)
    print("Concepts loaded: %s" % data)

def TestCollectionManager():
    from CollectionManager import CollectionManager
    cm = CollectionManager()
    cm.LoadCollections(collections)
    while True:
        cm.FrequencyOfWord(GetInputWord())
        if not TryAgain():
            break

def TestCompoundHandler():
    from CompoundHandler import CompoundHandler
    print("Result of CompoundHandler: ")

    ch = CompoundHandler(useWordVectors = USEWORDVECTORS, wordVectorWeight = WORDVECTOR_WEIGHT,
                         useWordNet = USEWORDNET, wordNetWeight = WORDNET_WEIGHT,
                         totalWeight = TOTAL_WEIGHT)
    while True:
        compoundA = input("Enter the first possibly compound term: ")
        compoundB = input("Enter the second possibly compound term: ")
        if s.Setting("reload") is True:
            s.LoadSettings()
        print(ch.GetSimilarity(compoundA, compoundB))
        if not TryAgain():
            break

def TestExternalCompounds():
    import numpy

    from CompoundHandler import CompoundHandler
    ch = CompoundHandler(useWordVectors = USEWORDVECTORS, wordVectorWeight = WORDVECTOR_WEIGHT,
                         useWordNet = USEWORDNET, wordNetWeight = WORDNET_WEIGHT,
                         totalWeight = TOTAL_WEIGHT)

    from JsonParser import JsonParser
    jp = JsonParser()
    data = jp.LoadFile(COMPOUNDSFILE)

    

    while True:
        if s.Setting("reload") is True:
           s.LoadSettings()

        results = []

        for value in data:
            print("== Comparing %s to %s. ==" % (value["one"], value["two"]))
            result = ch.GetSimilarity(value["one"], value["two"])
            results.append(abs(value["sim"] - result))
            print("Similarity expected - found: %s - %s\n" % (value["sim"], result))

        print("Average distance: %s - Standard deviation: %s" % (numpy.mean(results), numpy.std(results)))
        print("==============================")
        print()

        if not TryAgain():
            break

def IsValidChoice(choice):
    if(choice=="a" or choice=="b" or choice=="c" or choice=="d" or choice=="e" or choice=="f" or choice=="g" or choice=="h"):
        return True
    else:
        return False

def GetInputWord():
    input = input("Enter a concept to put into this test (i.e. Aeroplane): ")
    if s.Setting("reload") is True:
        s.LoadSettings()
    return input

def TryAgain():
    return input("Do you want to try again? (y/n) ") == "y"

Main()