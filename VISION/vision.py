#!/usr/bin/env python3

import numpy as np
import matplotlib as plt
import random, os
import tensorflow as tf
import cv2
from keras.models import load_model
from keras.applications import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing.image import ImageDataGenerator



def splitTestTrain():
	path = "original-jpegs" #Nombre de la carpeta de todas las imagenes
	trainImages = []
	testImages = []

	#Se crea un directorio con los subdirectorios test y train
	try:	
		os.mkdir('splitImages')
		os.mkdir('splitImages/train')
		os.mkdir('splitImages/test')
		os.mkdir('splitImages/valid')
		print("Los directorios se han creado correctamente")
	
	except FileExistsError:
		print ("El directorio ya existe")


	if len(os.listdir('splitImages/train/')):
		print ("El directorio ya tiene fotos.")
	else:
	
		#Lista de rutas de cada imagen
		for root, dirs, files in os.walk(path):
			for name in files:
				if name.endswith(".jpg"):
					trainImages.append(root+'/'+name)
					

		#Se selecciona el 20% de imágenes aleatoriamente y se eliminan de train
		random.shuffle(trainImages)
		testImages = trainImages[0:int(len(trainImages)*0.2)]
		del trainImages[0:int(len(trainImages)*0.2)]
		print(len(testImages),len(trainImages))
	
		#Se copian las imagenes en las carpetas de train y test, y se seleccionan 6 para el parterre	
		i=0	
		for image in testImages:
			os.system('cp '+image+' splitImages/test/'+str(i)+'.jpg')
			i+=1
		i=0
		for image in trainImages:
			os.system('cp '+image+' splitImages/train/'+str(i)+'.jpg')
			i+=1
		i=0
		for image in testImages[0:6]:
			os.system('cp '+image+' splitImages/valid/'+str(i)+'.jpg')
			i+=1
	
		
			

def CNN():
	model = load_model('TF_85.h5')
	#model.summary()
	model.trainable = False #Se ha entrenado la red en Google Collab
	
	imNum = 0
	classList = []
	while imNum < 6:
		img=cv2.imread('splitImages/valid/'+str(imNum)+'.jpg')
		img = cv2.resize(img,(150,150))
		img = np.reshape(img,[1,150,150,3])

		flowerClass = np.asarray((model.predict(img)).tolist(),dtype=np.int)
		
		correctClass = 0

		for c in flowerClass[0]:
			if c>0:				
				imNum+=1
				break
			
			else:
				correctClass+=1
				

		# Clases (una para cada una de las 6 flores):
		# 0 - Margarita
		# 1 - Diente de leon
		# 2 - Rosa
		# 3 - Girasol
		# 4 - Tulipan		
		classList.append(correctClass) # de dimensión [1x6]
	print(classList)



def main():
	splitTestTrain()
	CNN()

if __name__ == "__main__":
	main()
