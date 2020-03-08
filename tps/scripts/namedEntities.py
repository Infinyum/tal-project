import sys

path = sys.argv[1]

file = open(path,'r+')

n = 0 # Number of named entities
entityByType = {}

for line in file:
	words = line.split(" ")
	for word in words:
		entity = word.split("/")
		
		if (len(entity) == 2):
			if (entity[1] != 'O'):
				if (entity[1] in entityByType):
					# append the new entity to the existing array for this entity type
					entityByType[entity[1]].append(entity[0])
				else:
					# create a new array for this entity type
					entityByType[entity[1]] = [entity[0]]
				
				n += 1

#print("Entity\tType\tOccurences\tProportion")
print("{:>15} {:>12} {:>12} {:>15}".format("Entity", "Type", "Occurences", "Proportion") + "\n")

for eType in entityByType:
	entities = entityByType[eType]
	for e in list(set(entities)):
		occ = entities.count(e)
		proportion = str(occ) + "/" + str(n)  + " (" + "{0:.2f}".format((occ/n)*100) + "%)"
		print('{:>15}  {:>12}  {:>12} {:>15}'.format(e, eType, str(occ), proportion))

file.close()