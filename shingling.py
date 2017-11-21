#http://codegists.com/snippet/python/k-shingling-pythonpy_renien_python
#http://stuartmyles.blogspot.in/2012/07/shingling-in-python.html
#http://ethen8181.github.io/machine-learning/clustering_old/text_similarity/text_similarity.html#k-shingling
ShingleSize = 5
def ComputeShingles(data):
	shingles = set()
	lenData = len(data)
	if(len < ShingleSize):
		print("shingles are not possible!!")
		pass
	else:
		for idx , token in enumerate(data):
			if((idx + ShingleSize) <= lenData):
				newShingle = data[idx : idx + ShingleSize]
				shingles.add(newShingle)
		#shingleArr=[]
		#for i in shingles:
		#	shingleArr.append(i)
		#return shingleArr
		return shingles

def parseMessage(data):
	parsedMessage = ""
	lenData = len(data)
	for idx , token in enumerate(data):
		if(data[idx] != '.' and data[idx] != ',' and data[idx] != ' ' and 
			data[idx] != '-' and data[idx] != '(' and data[idx] != ')'):
			parsedMessage += (data[idx])
	return parsedMessage


UniqueShingles = set()
MatrixBeg = []
count = 0
for i in range(1,4):
	FileName = "test" + str(i) + ".txt"
	#print(FileName)
	readtextFile = open(FileName,'r')
	message = readtextFile.read()
	message = parseMessage(message)
	#print(message)
	
	shingles = ComputeShingles(message)
	#print(shingles)
	readtextFile.close()
	
	FileName = "shingles" + str(i) + ".txt"
	#print(FileName)
	countOfShingles = 0
	writeTextFile = open(FileName,'w')
	for shingle in shingles:
		countOfShingles += 	1
		if(shingle not in UniqueShingles):
			MatrixBeg.append([shingle,count])
			count += 1
			UniqueShingles.add(shingle)
		writeTextFile.write(shingle)
		writeTextFile.write("\n")
	#print(countOfShingles) #2353 2725 2077
	writeTextFile.close()
#print(len(UniqueShingles))
print(len(MatrixBeg))
charactersticMatrix = []
for i in MatrixBeg:
	print(i)
