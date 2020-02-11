import sys

from nltk.tokenize import word_tokenize
from nltk import pos_tag

inputPath = sys.argv[1]
outputPath = sys.argv[2]

inputFile = open(inputPath, "r+")
outputFile = open(outputPath, 'w')

for line in inputFile:
    tokenizedText = word_tokenize(line)
    tokensTagged = pos_tag(tokenizedText)
    
    for tokenTuple in tokensTagged:
        outputFile.write(tokenTuple[0] + "\t" + tokenTuple[1] + "\n")

inputFile.close()
outputFile.close()