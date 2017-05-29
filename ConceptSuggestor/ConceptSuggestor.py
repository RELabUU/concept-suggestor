COMMITFILE = "commit_example2.json" # Example commit to load
CONCEPTSFILE = "concepts_example.json" # Example concepts already in the model
OUTFILE = "suggestions_example.json" # Example file to send after request

WORDVECTOR_THRESHOLD = 0.9
TOTAL_THRESHOLD = 0.8

WORDVECTOR_WEIGHT = 0.5
THESAURUS_WEIGHT = 0.5
WORDNET_WEIGHT = 0.5
TOTAL_WEIGHT = WORDVECTOR_WEIGHT + THESAURUS_WEIGHT + WORDNET_WEIGHT

def IsValidChoice(choice):
    if(choice=="a" or choice=="b" or choice=="c" or choice=="d" or choice=="e"):
        return True
    else:
        return False

def GetProgramMode():
    print("These are your options:")
    print("a - The complete parameterized package. Loads new concepts from external JSON file, adds non-synonyms to the existing concepts, and writes that to an external JSON file.")
    print("b - Check similarity using word vectors.")
    print("c - Check whether a synonym exists using thesaurus.com.")
    print("d - Check whether a synonym exists using WordNet.")
    print("e - Open a JSON file.")

    # Get the program mode from the user and ensure it's valid.
    choice = input("Please tell me what to do (type a letter): ").lower()
    if(IsValidChoice(choice)):
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
    if(choice != "a" and choice != "e"):
        new = input("Enter a concept you want to check whether we have a synonym for (i.e. Aeroplane): ")

    if(choice == "a"):
        from SynonymRemover import SynonymRemover
        sr = SynonymRemover(concepts, TOTAL_THRESHOLD, 
                            useWordVectors = True, wordVectorWeight = WORDVECTOR_WEIGHT,
                            useThesaurus = True, thesaurusWeight = THESAURUS_WEIGHT, 
                            useWordNet = True, wordNetWeight = WORDNET_WEIGHT,
                            totalWeight = TOTAL_WEIGHT, totalThreshold = TOTAL_THRESHOLD)
        
        from JsonParser import JsonParser
        jp = JsonParser()
        newConcepts = jp.LoadCommit(COMMITFILE)

        finalConcepts = sr.AddWithoutSynonyms(concepts, newConcepts)

        print("Final concepts: %s" % finalConcepts)
        jp.MakeFile(finalConcepts, OUTFILE)

    elif(choice == "b"):
        from SemanticSimilarity import SemanticSimilarity
        print("Result of semantic similarity: ")
        ss = SemanticSimilarity(concepts)
        print(ss.HasSynonym(new, WORDVECTOR_THRESHOLD))

    elif(choice=="c"):
        from ThesaurusSynonyms import ThesaurusSynonyms
        print("Result of Thesaurus.com synonyms: ")
        ds = ThesaurusSynonyms()
        print(ds.HasSynonym(new, concepts))

    elif(choice=="d"):
        from WordNetSynonyms import WordNetSynonyms
        print("Result of WordNet synonyms: ")
        wns = WordNetSynonyms()

        print(wns.HasSynonym(new, concepts))

    elif(choice=="e"):
        from JsonParser import JsonParser
        print("Result of JsonParser: ")
        jp = JsonParser()
        data = jp.LoadCommit(COMMITFILE)
        print(data)
        jp.MakeFile(data, OUTFILE)
    else:
        print("Invalid mode. Aborting.")

Main()