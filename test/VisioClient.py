import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    plant=data.decode('ascii')
    # print("La planta a ver es: ", plant)
    ele=plant[7:8]
    # print(ele)
    ele = int(ele)
    print("Planta elegida: ", ele)
    print("Enviando información a el servidor...")
    s.sendall(b'Densidad foliar= 23, Salud = 56')
    s.close()
    # Prop = b'050-025' 
    # s.sendall(Prop)