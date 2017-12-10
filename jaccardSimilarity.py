#https://gist.github.com/ariezncahyo/7fa9c0a88b474a1b5f3b72e4d9650292
#http://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_similarity_score.html
#http://love-python.blogspot.in/2012/07/python-code-to-compute-jaccard-index.html
from sklearn.metrics import jaccard_similarity_score
#from shingling import sigMatrix
from math import *
import csv
#print(sigMatrix)
#print(len(sigMatrix))
#for i in range(sigMatrix):
#	for j in range()
def ComputeScore(set1 , set2):
	#print(set1)
	#print(set2)
	Intersection = len(set(set1).intersection(set2))
	Union = len(set(set1).union(set2))
	score = Intersection / float(Union)
	#print(score)
	score = round(score , 5)
	return score
	

def computejaccardSimilarity(signatureMatrix):
	similarityMat = []
	similarityMat2 = []
	for i in range(5):
		for j in range(i + 1 , 5):
			set1 = signatureMatrix[i]
			set2 = signatureMatrix[j]
			score = ComputeScore(set1 , set2)
			scoreauto = jaccard_similarity_score(set1 , set2)
			similarityMat.append(score)
			scoreauto = round(scoreauto , 5)
			similarityMat2.append(scoreauto)
	return similarityMat , similarityMat2

sigMatrix = []
signatureMatrixFile = open("SignatureMatrix.txt","r")
matrixReader = csv.reader(signatureMatrixFile , delimiter = ' ')
for row in matrixReader:
	sigMatrix.append(row)


jaccardSimilarity,jaccardSimilarityAuto = computejaccardSimilarity(sigMatrix)
print("Manually calculated:" , jaccardSimilarity)
print("Model calculated:" , jaccardSimilarityAuto)
