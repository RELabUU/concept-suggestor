from Settings import Settings
settings = Settings()

COMMITFILE = "commit_example2.json" # Example commit to load
CONCEPTSFILE = "concepts_example.json" # Example concepts already in the model
OUTFILE = "suggestions_example.json" # Example file to send after request
AIRMFILE = "AIRM/EA4A02.informationmodel.xml" # AIRM information model
COMPOUNDSFILE = "compound_concepts.json" # File containing compound words and their human-estimated similarity.

collections = { "one": "concepts_example.json",
                "two": "concepts_example2.json" }

def GetProgramMode():
    print("These are your options:")
    print("a - Example Functionality. Loads new concepts from external JSON file, removes synonyms, and writes that to an external JSON file.")
    print("b - Compare similarity of two words using SpaCy's word vectors.")
    print("c - Compare similarity of two words using WordNet's similarity function.")
    print("d - Uses WordNet to determine whether two words are synonyms.")
    print("e - Compares two possibly compound terms and returns the similarity between them.")
    print("f - Tests compound terms found in compound_concepts.json for similarity.")

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
        TestSpacySimilarity()
    elif choice == "c":
        TestWordNetSimilarity()
    elif choice == "d":
        TestWordNetSynonymity()
    elif choice == "e":
        TestCompoundHandler()
    elif choice == "f":
        TestExternalCompounds()
    else:
        print("Invalid mode. Aborting.")

def LoadConcepts():
    from JsonParser import JsonParser

    jp = JsonParser()

    return jp.LoadFile(CONCEPTSFILE, debug = True) # DEBUG - Not the entire line, only the "debug = True" part.

def TestCompletePackage(existingConcepts):
    from SynonymRemover import SynonymRemover
    sr = SynonymRemover(existingConcepts, settings)
        
    from JsonParser import JsonParser
    jp = JsonParser()
    newConcepts = jp.LoadCommit(COMMITFILE)

    newConcepts = sr.RemoveSynonyms(existingConcepts, newConcepts)

    print("New concepts: %s" % newConcepts)
    jp.MakeFile(newConcepts, OUTFILE)

def TestSpacySimilarity():
    from SpacySimilarity import SpacySimilarity
    ss = SpacySimilarity()

    while True:
        wordA = GetInputWord()
        if wordA != "n":
            wordB = GetInputWord()
            if wordB != "n":
                print("%s <> %s: %f" % (wordA, wordB, ss.GetSimilarity(wordA, wordB)))
            else:
                break
        else:
            break

def TestWordNetSimilarity():
    from WordNetSimilarity import WordNetSimilarity
    wns = WordNetSimilarity(settings.WordNetSimilarityMethod())

    while True:
        wordA = GetInputWord()
        if wordA != "n":
            wordB = GetInputWord()
            if wordB != "n":
                print("%s <> %s: %f" % (wordA, wordB, wns.GetSimilarity(wordA, wordB)))
            else:
                break
        else:
            break

def TestWordNetSynonymity():
    from WordNetSynonyms import WordNetSynonyms
    wns = WordNetSynonyms()

    while True:
        wordA = GetInputWord()
        if wordA != "n":
            wordB = GetInputWord()
            if wordB != "n":
                print("%s <> %s: %s" % (wordA, wordB, wns.IsSynonym(wordA, wordB)))
            else:
                break
        else:
            break

def TestCompoundHandler():
    from CompoundHandler import CompoundHandler
    ch = CompoundHandler(settings)
    print("Result of CompoundHandler: ")

    while True:
        compoundA = input("Enter the first possibly compound term (type \"n\" to quit): ")
        if compoundA != "n":
            compoundB = input("Enter the second possibly compound term: ")
            if settings._Setting("reload") is True:
                settings.LoadSettings()
            print(ch.GetSimilarity(compoundA, compoundB))
        else:
            break

def TestExternalCompounds():
    import numpy

    from CompoundHandler import CompoundHandler
    ch = CompoundHandler(settings)

    from JsonParser import JsonParser
    jp = JsonParser()
    data = jp.LoadFile(COMPOUNDSFILE)

    while True:
        if settings._Setting("reload") is True:
           settings.LoadSettings()

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
    if(choice=="a" or choice=="b" or choice=="c" or choice=="d" or choice=="e" or choice=="f"):
        return True
    else:
        return False

def GetInputWord():
    while True:
        concept = input("Enter a concept to put into this test (type \"n\" to quit): ")
        if concept == "":
            print("No concept was found. Please try again.")
            continue
        if settings.Reload() is True:
            settings.LoadSettings()
        return concept

def TryAgain():
    while True:
        tryagain = input("Do you want to try again? (y/n) ")
        if tryagain == "y":
            return True
        elif tryagain == "n":
            return False
        else:
            print("Could not understand. Please try again. Type \"y\" or \"n\".")

Main()