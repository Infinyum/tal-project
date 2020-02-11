import sys

intputPath = sys.argv[1]
outputPath = sys.argv[2]

inputFile = open(intputPath,'r+')
outputFile = open(outputPath, 'w+')

entity = ""
label = ""

for line in inputFile:
	if line[0] != "#" and line != "\n":
		words = line.split("\t")
		
		if (len(words) >= 4):
			entity = words[1]
			label = words[3]
			outputFile.write(entity + '\t' + label + '\n')
	
inputFile.close()
outputFile.close()