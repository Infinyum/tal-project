import sys

from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk import ne_chunk

inputPath = sys.argv[1]
outputPath = sys.argv[2]

inputFile = open(inputPath, "r+")
#outputFile = open(outputPath, 'w')

for line in inputFile:
    tokenizedText = word_tokenize(line)
    tokensTagged = pos_tag(tokenizedText)
    namedEnt = ne_chunk(tokensTagged, binary=False)

    for tokenNe in namedEnt:
        if type(tokenNe).__name__ == "Tree":
            print(tokenNe)
            lb = tokenNe.label()

            if lb == "ORGANIZATION":
                print("ORG SPOTTED!")
            elif lb == "PERSON":
                print("PERSON SPOTTED!")
            elif lb == "GPE":
                print("LOCATION SPOTTED!")
            else:
                print("SOMETHING ELSE: " + lb)
        
        #print(list(tokenNe))
        #print(tokenNe[0] + "/" + tokenNe[1])


    #for tokenTuple in tokensTagged:
    #    outputFile.write(tokenTuple[0] + "\t" + tokenTuple[1] + "\n")

inputFile.close()
#outputFile.close()