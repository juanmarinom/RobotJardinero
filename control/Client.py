import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    dest = data.decode('ascii')
    PosX = dest[0:3]
    PosY = dest[4:7]
    PosZ =dest[8:11]
    print(PosX)
    print(PosY)
    print(PosZ)
