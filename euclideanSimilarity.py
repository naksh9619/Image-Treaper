import csv
import math
import distance
frequency = []
frequencyMatrixFile = open("FrequencyMatrix.txt" , "r")
matrixReader = csv.reader(frequencyMatrixFile , delimiter = ' ')
for row in matrixReader:
	frequency.append(row)

def ComputeScore(set1 , set2):
	score = 0
	for set1Ele , set2Ele in zip(set1 , set2):
		tempScore = (int(set1Ele) - int(set2Ele)) * (int(set1Ele) - int(set2Ele))
		score += tempScore
	score = math.sqrt(score)
	score = round(score , 5)
	return score


def computeeuclideanSimilarity(freqMatrix):
	similarityMat = []
	similarityMat2 = []
	for i in range(1,6):
		for j in range(i + 1 , 6):
			set1 = freqMatrix[i]
			set2 = freqMatrix[j]
			score = ComputeScore(set1 , set2)
			scoreAuto = ComputeScore(set1 , set2)
			round(scoreAuto , 5)
			similarityMat.append(score)
			similarityMat2.append(scoreAuto)
	return similarityMat,similarityMat2


euclideanSimilarity , euclideanSimilarityAuto = computeeuclideanSimilarity(frequency)
print("Manually calculated:" , euclideanSimilarity)
print("Model calculated:" , euclideanSimilarityAuto)