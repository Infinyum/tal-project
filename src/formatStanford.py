import sys

# Opening files
inputPath = sys.argv[1]
inputFile = open(inputPath,'r')
outputPath = sys.argv[2]
outputFile = open(outputPath, "w+")

# Conversion
for line in inputFile:
	words = line.split(" ")
	for word in words:
		wordLabel = word.split("_")
		if (len(wordLabel) == 2):
			outputFile.write(wordLabel[0] + '\t' + wordLabel[1] + '\n')

inputFile.close()
outputFile.close()