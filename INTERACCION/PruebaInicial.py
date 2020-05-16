#Imports modules
import socket
import time


listensocket = socket.socket() #Creates an instance of socket
Port = 8000 #Port to host server on
maxConnections = 999
IP = socket.gethostname() #IP address of local machine

listensocket.bind(('',Port))

#Starts server
listensocket.listen(maxConnections)
print("Server started at " + IP + " on port " + str(Port))

#Accepts the incomming connection
(clientsocket, address) = listensocket.accept()
print("New connection made!")



message = clientsocket.recv(1024).decode() #Gets the incomming message
print(message)
Name = input("Please enter your name?")
print("sending"+Name)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 8000))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print("end")