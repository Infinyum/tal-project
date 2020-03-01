import sys

path = sys.argv[1]
pathOut = sys.argv[2]

file = open(path,'r+')
fileOut = open(pathOut, 'w')

n = 0 # Number of named entities
entityByType = {}
entity = ""
entityType = ""

for line in file:
	# Ignore comments and empty lines
	if line[0] != '#' and line[0] != '\n':
		words = line.split("\t")
		
		if (len(words) >= 2):
			entity = words[1]
			rawEntityType = words[-1]

			if ("NE=" in rawEntityType):
				entityType = rawEntityType[rawEntityType.find('.')+1:rawEntityType.find('|')]
			else:
				entityType = "O"
			fileOut.write(entity + "\t" + entityType + "\n")
		

file.close()
fileOut.close()