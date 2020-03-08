import sys

path = sys.argv[1]
pathOut = sys.argv[2]

file = open(path,'r+')
fileOut = open(pathOut, 'w')

entity = ""
label = ""

for line in file:
	words = line.split("\t")
	
	if (len(words) >= 4):
		entity = words[1]
		label = words[3]
		fileOut.write(entity + '\t' + label + '\n')
	
file.close()
fileOut.close()