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
    existingConcepts = jp.LoadFile(CONCEPTSFILE)
    print("Concepts already in the model: %s" % existingConcepts)

    choice = GetProgramMode()

    if choice == "a":
        TestCompletePackage(existingConcepts)
    elif choice == "b":
        TestSpacySimilarity(existingConcepts, GetInputWord())
    elif choice=="c":
        TestThesaurusSynonyms(existingConcepts, GetInputWord())
    elif choice=="d":
        TestWordNetSimilarity(existingConcepts, GetInputWord())
    elif choice=="e":
        TestJsonParser()
    elif choice=="f":
        TestXmlParser()
    elif choice=="g":
        TestCollectionManager(GetInputWord())
    elif choice=="h":
        TestCompoundHandler()
    else:
        print("Invalid mode. Aborting.")

def GetInputWord():
    return input("Enter a concept to put into this test (i.e. Aeroplane): ")

def TestCompletePackage(existingConcepts):
    from SynonymRemover import SynonymRemover
    sr = SynonymRemover(existingConcepts, TOTAL_THRESHOLD, 
                        useWordVectors = USEWORDVECTORS, wordVectorWeight = WORDVECTOR_WEIGHT,
                        useThesaurus = USETHESAURUS, thesaurusWeight = THESAURUS_WEIGHT, 
                        useWordNet = USEWORDNET, wordNetWeight = WORDNET_WEIGHT,
                        totalWeight = TOTAL_WEIGHT, totalThreshold = TOTAL_THRESHOLD)
        
    from JsonParser import JsonParser
    jp = JsonParser()
    newConcepts = jp.LoadCommit(COMMITFILE)

    newConcepts = sr.RemoveSynonyms(existingConcepts, newConcepts)

    print("New concepts: %s" % newConcepts)
    jp.MakeFile(newConcepts, OUTFILE)

def TestSpacySimilarity(existingConcepts, newWord):
    from SpacySimilarity import SpacySimilarity
    print("Result of semantic similarity: ")
    ss = SpacySimilarity(existingConcepts)
    print(ss.HasSynonym(newWord, WORDVECTOR_THRESHOLD))

def TestThesaurusSynonyms(existingConcepts, newWord):
    from ThesaurusSynonyms import ThesaurusSynonyms
    print("Result of Thesaurus.com synonyms: ")
    ds = ThesaurusSynonyms()
    print(ds.HasSynonym(newWord, existingConcepts))

def TestWordNetSimilarity(existingConcepts, newWord):
    from WordNetSimilarity import WordNetSimilarity
    print("Result of WordNet similarity: ")
    wns = WordNetSimilarity()
    print(wns.GetMaxSimilarity(newWord, existingConcepts))

def TestJsonParser():
    from JsonParser import JsonParser
    print("Result of JsonParser: ")
    jp = JsonParser()
    data = jp.LoadCommit(COMMITFILE)
    print(data)
    jp.MakeFile(data, OUTFILE)

def TestXmlParser():
    from XmlParser import XmlParser
    print("Result of XmlParser: ")
    xp = XmlParser()
    data = xp.LoadFile(AIRMFILE)
    print(data)

def TestCollectionManager(word):
    from CollectionManager import CollectionManager
    print("Result of CollectionManager: ")
    cm = CollectionManager()
    cm.LoadCollections(collections)
    print(cm.FrequencyOfWord(word))

def TestCompoundHandler():
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

Main()