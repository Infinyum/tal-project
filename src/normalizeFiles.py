import sys

#We read the path of the file to convert to the universal tokenisation
pathRef = sys.argv[1];
path2 = sys.argv[2];

#We open all the files
ref = open(pathRef, 'r')
file2 = open(path2, 'r')
FO = open('normalized.txt', 'w')


#We manually map each value of the reference
labelMap = {}
for line in ref:
    arrLine = line.split()
    key = arrLine[0]
    val = arrLine[1]
    labelMap[key] = val

#Then we compare to the actual file
for line in file2:
    arrLine = line.split()
    key = arrLine[0]
    val = arrLine[1]
    if labelMap.__contains__(key):
      labelMap[key]=val

#We write everything to the outfile
for cle,valeur in labelMap.items():
        FO.write(cle+'\t'+valeur+'\n')


FO.close()
ref.close()
file2.close()
