import base64

for i in range(1 , 6):
	fileName = "img" + str(i) + ".jpg"
	print("Processing image: " , fileName)
	imageFile = open("images/" + fileName , "rb")
	stringImage = base64.b64encode(imageFile.read())
	#print(stringImage)
	imageFile.close()

	fileName = "test" + str(i) + ".txt"
	writeFile = open("testFiles/" + fileName , "w")
	for text in stringImage:
		writeFile.write(text)
	writeFile.close()