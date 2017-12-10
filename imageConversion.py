import base64
from PIL import Image
for i in range(1 , 6):

	fileName = "img" + str(i) + ".jpg"
	print("Processing image: img"+str(i))
	imgOpen=Image.open("images/" + fileName)
	#a,b=imgOpen.size()
	#print(a,b)
	fileName="img"+str(i)+".jpg"
	imgOpen.save("images/" + fileName,optimize=True,quality=40)
	#print(imgOpen.size())
	imgOpen.close()
	imageFile = open("images/" + fileName , "rb")
	stringImage = base64.b64encode(imageFile.read())
	#print(stringImage)
	imageFile.close()

	fileName = "test" + str(i) + ".txt"
	writeFile = open("testFiles/" + fileName , "w")
	for text in stringImage:
		writeFile.write(text)
	writeFile.close()
