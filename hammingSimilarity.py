

def parseMessage(data):
	parsedMessage = ""
	lenData = len(data)
	for idx , token in enumerate(data):
		if(data[idx] != '.' and data[idx] != ',' and data[idx] != ' ' and 
			data[idx] != '-' and data[idx] != '(' and data[idx] != ')' and data[idx] != '/' and data[idx] != '+' and data[idx] != '='):
			parsedMessage += (data[idx])
	return parsedMessage

def getStrings():
	stringArray = []
	for i in range(1 , 6):
		FileName = "test" + str(i) + ".txt"
		readtextFile = open("testFiles/" + FileName , 'r')
		message = readtextFile.read()
		message = parseMessage(message)
		stringArray.append(message)
		readtextFile.close()
	return stringArray

def padExtra(set1 , set2):
	extra = len(set2) - len(set1)
	for i in range(extra):
		set1+="1"
	return set1 , set2

def ComputeScore(set1 ,set2):
	score = 0
	#print("length before:",len(set1) , len(set2))
	if(len(set1) > len(set2)):
		set1 , set2 = set2 , set1
	if(len(set1) != len(set2)):
		set1 , set2 = padExtra(set1 , set2)
	for set1Char,set2Char in zip(set1 , set2):
		if(set1Char != set2Char):
			score += 1
	#print("length after:" , len(set1) , len(set2) , score)
	return score

def getHammingSimilarity(stringArray):
	similarityMat = []
	for i in range(4):
		for j in range(i + 1 , 5):
			score = ComputeScore(stringArray[i] , stringArray[j])
			similarityMat.append(score)
	return similarityMat

stringArray = getStrings()
hammingSimilarity = getHammingSimilarity(stringArray)
print("Manually calculated:" , hammingSimilarity)