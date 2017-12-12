#from shingling import frequency
from sklearn.metrics.pairwise import cosine_similarity
import math
import csv

def ComputeScore(set1 , set2):
	#cosineSimilarity=summation of set1[i]*set2[i]/|set1|*|set2|
	#print(set1)
	#print(set2)
	dotProduct=0
	for i , j in zip(set1 , set2):
		dotProduct += (int(i) * int(j))
	#print(dotProduct)
	set1Sum = 0
	set2Sum = 0
	for i in set1:
		set1Sum += (int(i) * int(i))
	for i in set2:
		set2Sum += (int(i) * int(i))
	set1Sum = math.sqrt(set1Sum)
	set2Sum = math.sqrt(set2Sum)
	denom = set2Sum * set1Sum
	if(denom == 0):
		return 0
	score = dotProduct / denom
	#print(dotProduct,set1Sum,set2Sum,denom)
	score = round(score , 5)
	return score

def computecosineSimilarity(freqMatrix):
	similarityMat = []
	similarityMat2 = []
	for i in range(1,6):
		for j in range(i + 1 , 6):
			set1 = freqMatrix[i]
			set2 = freqMatrix[j]
			score = ComputeScore(set1 , set2)
			#scoreauto = cosine_similarity(set1 , set2)
			scoreauto = ComputeScore(set1 , set2)
			scoreauto = round(score , 5)
			similarityMat.append(score)
			similarityMat2.append(scoreauto)
	return similarityMat , similarityMat2

frequency = []
frequencyMatrixFile = open("FrequencyMatrix.txt" , "r")
matrixReader = csv.reader(frequencyMatrixFile , delimiter = ' ')
for row in matrixReader:
	frequency.append(row)

'''
ok=0
for i in range(len(frequency)):
	for j in range(len(frequency[i])):
		if(frequency[i][j]==0):
			ok=1
			break
if(ok):
	print("i am here")

for i in range(len(frequency)):
	countNonZero = 0
	for j in range(len(frequency[i])):
		if(frequency[i][j]):
			countNonZero+=1
	print("NonZero in row " + str(i) + " are " ,countNonZero)
#print(frequency)
'''
cosinesimilarity , cosinesimilarityAuto = computecosineSimilarity(frequency)
print("Manually calculated:" , cosinesimilarity)
print("Model calculated:" , cosinesimilarityAuto)