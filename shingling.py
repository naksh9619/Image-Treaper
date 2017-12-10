#http://codegists.com/snippet/python/k-shingling-pythonpy_renien_python
#http://ethen8181.github.io/machine-learning/clustering_old/text_similarity/text_similarity.html#k-shingling4
#http://dspace.thapar.edu:8080/jspui/bitstream/10266/4043/4/4043.pdf
import csv
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
			data[idx] != '-' and data[idx] != '(' and data[idx] != ')' and data[idx] != '/' and data[idx] != '+' and data[idx] != '='):
			parsedMessage += (data[idx])
	return parsedMessage


def hash1(val):
	result = (val + 3) % 1000000007
	return result


def hash2(val):
	result = (105 * val + 1) % 1000000007
	return result


def hash3(val):
	result = (1017 * val + 1) % 1000000009
	return result


def hash4(val):
	result = (1439 * val + 1) % 786543
	return result


def hash5(val):
	result = (5821*val + 1) % 456783
	return result 


#using Min hash algorithm to find signature matrix
def findsignatureMatrix(data , args):
	rows = len(data)
	cols = len(data[0])
	sigrows = len(args)
	#print(sigrows)
	signatureMatrix = []
	for _ in range(sigrows):
		signatureMatrix.append([9999999999] * cols)
	for row in range(rows):
		 Hash = map(lambda x : x(row) , args)
		 for col in range(cols):
		 	if(data[row][col] != 0):
		 		for idx in range(sigrows):
		 			if(signatureMatrix[idx][col] > Hash[idx]):
		 				signatureMatrix[idx][col] = Hash[idx]
	return signatureMatrix



UniqueShingles = set()
MatrixBeg = []
count = 0
for i in range(1 , 6):
	FileName = "test" + str(i) + ".txt"
	#print(FileName)
	readtextFile = open("testFiles/" + FileName , 'r')
	message = readtextFile.read()
	message = parseMessage(message)
	#print(message)
	shingles = ComputeShingles(message)
	#print(shingles)
	#print(len(shingles))
	readtextFile.close()
	FileName = "shingles" + str(i) + ".txt"
	#print(FileName)
	countOfShingles = 0
	count = 0
	writeTextFile = open("shingleFiles/" + FileName , 'w')
	for shingle in shingles:
		countOfShingles += 	1
		if(shingle not in UniqueShingles):
			#print(shingle,count)
			MatrixBeg.append([shingle , count])
			count += 1
			UniqueShingles.add(shingle)
		writeTextFile.write(shingle)
		writeTextFile.write("\n")
		#print(count)
	#print(countOfShingles) #34848 21936 29824 37831 22803

	writeTextFile.close()
#print(len(UniqueShingles))
#print(len(MatrixBeg))
#print(MatrixBeg)
charactersticMatrix = [[0 for x in range(6)] for y in range(len(MatrixBeg))]
frequency = [[0 for x in range(len(MatrixBeg))] for y in range(6)]
for j in range(0,len(MatrixBeg)):
	checkChar = MatrixBeg[j][0]
	#print("iteration " + str(j))
	for i in range(1 , 6):
		FileName = "shingles" + str(i) + ".txt"
		readtextFile = open("shingleFiles/" + FileName , "r")
		message = readtextFile.read()
		message = message.split()
		if(checkChar in message):
			charactersticMatrix[j][i] = 1
			frequency[i][j] += 1
		readtextFile.close()

#print(charactersticMatrix)
'''for i in range(1 , 6):
	print("processing shingle" + str(i))
	FileName = "shingles" + str(i) + ".txt"
	readtextFile = open("shingleFiles/" + FileName,"r")
	message = readtextFile.read()
	#print(message)
	#print(len(message))
	message = message.split()
	res=0
	for j in range(0 , len(MatrixBeg)):
		#print("i am here",res)
		res+=1
		#print(MatrixBeg[j])
		if(MatrixBeg[j][0] in message):
			charactersticMatrix[j][i] = 1
			frequency[i][j] += 1
		#print("processing"+str(j))
	#print("end of shingle"+str(i))
	readtextFile.close()
'''
#for i in charactersticMatrix:
#	print(i)
#	print("\n")
#print(charactersticMatrix)

sigMatrix = findsignatureMatrix(charactersticMatrix, [hash1 , hash2 , hash3 , hash4 , hash5])
#print(sigMatrix)

for i in range( len(sigMatrix) ):
	sigMatrix[i][0] = 0


storeFrequencyMatrix = open("FrequencyMatrix.txt" , "w")
matrixWriter = csv.writer(storeFrequencyMatrix , delimiter = ' ')
for row in frequency:
	matrixWriter.writerow(row)
storeFrequencyMatrix.close()

storeSignatureMatrix = open("SignatureMatrix.txt" , "w")
matrixWriter = csv.writer(storeSignatureMatrix , delimiter = ' ')
for row in sigMatrix:
	matrixWriter.writerow(row)
storeSignatureMatrix.close()
#print(sigMatrix)


'''
counter = 0
TESTING DONE SHIGLING, CHARACTERSTIC MATRIX AND SIGNATUARE MATRIX ABSOUTELY CORRECT
for i in charactersticMatrix:
	print(i)
	counter += 1
	print("\n")
ok = 1
row = 999
for i in charactersticMatrix:
	res = 0
	for j in range(4):
		if(i[j] == 1):
			res += 1
			if(res == 2):
				row = i
				ok = 0
print(ok)
print(row)
print(charactersticMatrix)
for i in MatrixBeg:
	print(i)
'''