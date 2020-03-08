import sys

path = sys.argv[1]

file = open(path,'r+')

n = 0 # Number of named entities
entityByType = {}
entity = ""
entityType = ""

for line in file:
	words = line.split("\t")
	
	if (len(words) >= 2):
		entity = words[1]
	
	for word in words:
		if ("NE=" in word):
			entityType = word[word.find('.')+1:word.find('|')]
			if (entityType in entityByType):
				# append the new entity to the existing array for this entity type
				entityByType[entityType].append(entity)
			else:
				# create a new array for this entity type
				entityByType[entityType] = [entity]
			
			n += 1

print("Entity\tType\tOccurences\tProportion")
print("{:>15} {:>12} {:>12} {:>15}".format("Entity", "Type", "Occurences", "Proportion") + "\n")

for eType in entityByType:
	entities = entityByType[eType]
	for e in list(set(entities)):
		occ = entities.count(e)
		proportion = str(occ) + "/" + str(n)  + " (" + "{0:.2f}".format((occ/n)*100) + "%)"
		print('{:>15}  {:>12}  {:>12} {:>15}'.format(e, eType, str(occ), proportion))

file.close()