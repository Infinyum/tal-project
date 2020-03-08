import sys

def loadDict():
#Function to load the mapping between the Stanford tokenisation and the universal tokenisation

    mappingLabel  = open('POSTags_PTB_Universal_Linux.txt', 'r');
    labelMap = {};

    #We manually map each value
    for line in mappingLabel:
        arrLine = line.split();
        key = arrLine[0];
        val = arrLine[1];
        labelMap[key] = val;

    mappingLabel.close();
    return labelMap;


#We read the path of the file to convert to the universal tokenisation
path = sys.argv[1];

#We open this file
convertFile = open(path,'r');

#We load the dictionnary
labelMap = loadDict();
res = ""

#we then try to get the word and its previous token
for line in convertFile:
    words = line.split(" ")
    for word in words:
        wordLabel = word.split("_")
        if (len(wordLabel) == 2):
            if(wordLabel[0] == "."):
                res = res + ".\t.\n"
                continue
            #print("Mot : " + wordLabel[0] + ", label : " + str(labelMap.get(wordLabel[1])))
            #We add the res to the results
            res = res + wordLabel[0] + "\t" + str(labelMap.get(wordLabel[1])) + "\n"

convertFile.close()

resPath = sys.argv[2] #path[0:len(path)-3] + "res.txt"

#Write the res in a file
resFile = open(resPath, "w+")
resFile.write(res);
resFile.close();
