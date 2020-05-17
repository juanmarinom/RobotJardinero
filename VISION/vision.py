#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import random, os
import tensorflow as tf
from keras.applications import ResNet50
from keras.applications.resnet50 import preprocess_input
from keras.models import Sequential, load_model
from keras.layers import Dense, Flatten, Dropout
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import ServerClass
import socket
import MainFlowers


def selectImages():
	path = "original-jpegs" #Nombre de la carpeta de todas las imagenes
	testImages = []

	#Se crea un directorio con los subdirectorios test y train
	try:	
		os.mkdir('testImages')
		print("El directorio se ha creado correctamente.")
	
	except FileExistsError:
		print ("El directorio ya existe")


	#Lista de rutas de cada imagen
	for root, dirs, files in os.walk(path):
		for name in files:
			if name.endswith(".jpg"):
				testImages.append(root+'/'+name)
					

	#Se seleccionan el 6 imágenes aleatoriamente y se copian en la carpeta testImages
	random.shuffle(testImages)
	testImages = testImages[0:6]

	i=0
	
	for image in testImages[0:6]:
		os.system('cp '+image+' testImages/'+str(i)+'.jpg')
		i+=1
	
def imagesForCV():

	testImages = []
	path = 'imagenesSeleccionables'
	os.mkdir('imgFinal')
	#Lista de rutas de cada imagen
	for root, dirs, files in os.walk(path):
		for name in files:
			if name.endswith(".jpg"):
				testImages.append(root+'/'+name)
	random.shuffle(testImages)
	testImages = testImages[0:6]
	print (testImages)
	i=0	
	for image in testImages:
		os.system('cp '+image+' imgFinal/'+str(i)+'.jpg')
		i+=1			
			

def createCNN():

	
	# Create model
	model = Sequential()
	model.add(ResNet50(include_top=False, pooling='avg', weights='imagenet'))
	model.add(Dense(256, activation='relu'))
	model.add(Dropout(0.5))
	model.add(Dense(5, activation='softmax'))
	model.load_weights('best_87.hdf5')

	testFolder = 'testImages/'
	image_size = 224
	data_generator = ImageDataGenerator(preprocessing_function=preprocess_input)

	#data = recieveSocket()
	data= 1
	pos = int(data)

	
	#Del socket se reciben categoria y posicion. Si cualquiera es -1, es que se busca el otro dato	
	if pos>0 and pos<6:
		tipoPlanta=predict_pos(model,testFolder,pos)
		print(tipoPlanta)
		return tipoPlanta

	else:
		print("Los datos de posicion y categoria no tienen el formato correcto.")



def predict_cat(model,path,cat):

	posList = [] 

	for imNum in range (0,6):
		img=image.load_img(path+str(imNum)+'.jpg', target_size=(224,224))
		img=image.img_to_array(img)
		img=np.expand_dims(img,axis=0)
		img=preprocess_input(img)
		
		prediction = np.argmax(model.predict(img))
		
		if prediction==cat:
			posList.append(imNum)
		
	
	return posList


def predict_pos(model,path,pos):
	
	img=image.load_img(path+str(pos)+'.jpg', target_size=(224,224))
	img=image.img_to_array(img)
	img=np.expand_dims(img,axis=0)
	img=preprocess_input(img)

	prediction = np.argmax(model.predict(img))
		
	return prediction



def recieveSocket():

	HOST = '127.0.0.1'  # The server's hostname or IP address
	PORT = 65432        # The port used by the server

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	    s.bind((HOST, PORT)) #Creación del socket
	    s.listen()
	    conn,addr = s.accept()
	    data = conn.recv(1024) #Recibimiento de la información
	    data = data.decode('ascii')
	    print(data)
	    conn.sendall(b'1')
	    #conn.close()

	return data
		


def main():	

	selectImages()
	flower = createCNN()
	health, density = MainFlowers.Flower(flower)
	print (status)
	

if __name__ == "__main__":
	main()
