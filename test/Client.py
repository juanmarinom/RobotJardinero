import socket
import time

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("Conectado")

while True:
    sel = input("Seleccionar planta >> ")
    str = bytes(sel,'utf-8')
    print(str)
    s.sendall(str)
