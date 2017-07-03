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
    print("g - Full pipeline. Determines whether two words are similar enough but not synonyms.")
    print("h - Tests compound terms found in compound_concepts.json for similarity, but uses only random results.")

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
    elif choice == "g":
        TestPipeline()
    elif choice == "h":
        TestExternalCompoundsRandom()
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
        wordA = GetInputWord(1)
        if wordA != "n":
            wordB = GetInputWord(2)
            if wordB != "n":
                print("%s <> %s: %f" % (wordA, wordB, ss.GetSimilarity(wordA, wordB)))
            else:
                break
        else:
            break

def TestWordNetSimilarity():
    from WordNetSimilarity import WordNetSimilarity
    wns = WordNetSimilarity(settings.WordNetSimilarityMethod)

    while True:
        wordA = GetInputWord(1)
        if wordA != "n":
            wordB = GetInputWord(2)
            if wordB != "n":
                if settings.Reload is True:
                    wns.ReloadSettings(settings.WordNetSimilarityMethod)
                print("%s <> %s: %f" % (wordA, wordB, wns.GetSimilarity(wordA, wordB)))
            else:
                break
        else:
            break

def TestWordNetSynonymity():
    from WordNetSynonyms import WordNetSynonyms
    wns = WordNetSynonyms()

    while True:
        wordA = GetInputWord(1)
        if wordA != "n":
            wordB = GetInputWord(2)
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
            if settings.Reload is True:
                settings.LoadSettings()
                ch.ReloadSettings(settings)
            print(ch.GetSimilarity(compoundA, compoundB))
        else:
            break

def TestExternalCompounds():
    print("Loading libraries...")
    from scipy.stats.stats import pearsonr
    from CompoundHandler import CompoundHandler
    ch = CompoundHandler(settings)
    from JsonParser import JsonParser
    jp = JsonParser()
    data = jp.LoadFile(COMPOUNDSFILE)

    while True:
        if settings.Reload is True:
           settings.LoadSettings()
           ch.ReloadSettings(settings)

        expected = []
        results = []

        for value in data:
            print("== Comparing %s to %s. ==" % (value["one"], value["two"]))
            result = ch.GetSimilarity(value["one"], value["two"])
            print("Similarity expected - found: %s - %s\n" % (value["sim"], result))

            expected.append(value["sim"])
            results.append(result)

        print("Pearson correlation, 2-tailed p-value:")
        print(pearsonr(expected, results))
        print("==============================")
        print()

        if not TryAgain():
            break

def TestExternalCompoundsRandom():
    print("Loading libraries...")
    from numpy import random
    from scipy.stats.stats import pearsonr
    from JsonParser import JsonParser
    jp = JsonParser()
    data = jp.LoadFile(COMPOUNDSFILE)

    while True:
        expected = []
        results = []

        for value in data:
            print("== Comparing %s to %s. ==" % (value["one"], value["two"]))
            result = random.uniform(0.0, 1.0)
            print("Similarity expected - found: %s - %s\n" % (value["sim"], result))

            expected.append(value["sim"])
            results.append(result)

        print("Pearson correlation, 2-tailed p-value:")
        print(pearsonr(expected, results))
        print("==============================")
        print()

        if not TryAgain():
            break

def TestPipeline():
    from SimilarityCalculator import SimilarityCalculator
    sc = SimilarityCalculator(settings)
    from WordNetSynonyms import WordNetSynonyms
    wns = WordNetSynonyms()

    while True:
        wordA = GetInputWord(1)
        if wordA != "n":
            wordB = GetInputWord(2)
            if wordB != "n":
                if settings.Reload is True:
                    sc.ReloadSettings(settings)
                similarity = sc.GetSimilarity(wordA, wordB)
                print("Similarity: %f" % similarity)
                if similarity > settings.SimilarityThreshold:
                    synonymity = wns.IsSynonym(wordA, wordB)
                    print("Synonymity: %s" % synonymity)
                    if synonymity is True:
                        print("The words are both accepted in the model!")
                    else:
                        print("One of the words is not accepted. They are synonyms.")
                else:
                    print("The words are both accepted in the model!")
            else:
                break
        else:
            break

def IsValidChoice(choice):
    if(choice=="a" or choice=="b" or choice=="c" or choice=="d" or choice=="e" or choice=="f" or choice=="g" or choice=="h"):
        return True
    else:
        return False

def GetInputWord(count = 0):
    while True:
        if count == 0:
            concept = input("Enter a concept to put into this test (type \"n\" to quit): ")
        else:
            concept = input("Enter concept %i to put into this test (type \"n\" to quit): " % count)

        if concept == "":
            print("No concept was found. Please try again.")
            continue
        if settings.Reload is True:
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