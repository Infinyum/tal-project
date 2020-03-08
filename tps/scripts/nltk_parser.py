import sys

from nltk import pos_tag
from nltk import RegexpParser
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
  
lemmatizer = WordNetLemmatizer() 

inputPath = sys.argv[1]
outputPath = sys.argv[2]

patternsFile = open("grammars.txt", "r+")
inputFile = open(inputPath, "r+")
outputFile = open(outputPath, 'w')

for pattern in patternsFile:
    outputFile.write(pattern)
    
    for line in inputFile:
        tokenizedText = word_tokenize(line)
        tokensLemmatized = []

        for token in tokenizedText:
            tokensLemmatized.append(lemmatizer.lemmatize(token))

        tokensTagged = pos_tag(tokensLemmatized)

        chunker = RegexpParser(pattern)

        output = chunker.parse(tokensTagged)
        outputSplit = str(output).split("\n")
        
        for chunk in outputSplit:
            if ("Compound" in chunk):
                outputFile.write(chunk[2:] + "\n")
    
    outputFile.write("\n")


patternsFile.close()
inputFile.close()
outputFile.close()