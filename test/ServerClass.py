import socket
import sys

class Server:

    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 65432 
    global s
    MAX = 2
    connections = 0
    
    all_connections =[]
    all_address =[]
    
    #Constructor por defecto, llama a las funciones de creación, bind y se queda a la espera de que se estableezcan ambas conexiones
    def __init__(self):
       self.create_socket()
       self.bind_socket()
       self.accept_connections() 
      
    #creación del socket de tipo AF_INET/STREAM
    def create_socket(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
        except socket.error as msg:
            print("Socket connection error: " + str(msg))
            
    #Se hace un bind del puerto
    def bind_socket(self):
        try:
            print("Binding to port: " + str(self.PORT))
            
            
            self.s.bind((self.HOST,self.PORT))
            self.s.listen(self.MAX)#numero maximo de clientes
            
        except socket.error as msg:
            print("Binding error" + str(msg))
    
    #Acepta las conexiones guardando el id de la conexión y el adress en dos vectores     
    def accept_connections(self):
        for self.c in self.all_connections:
            self.c.close()
    
        del self.all_connections[:]
        del self.all_address[:]
        s=self.s
        print("Waiting for connections...")
        while self.connections < self.MAX:
            # try:
            conn, address = s.accept()
            s.setblocking(1)  # prevents timeout

            self.all_connections.append(conn)
            self.all_address.append(address)

            print("Connection has been established :" + address[0])
            self.connections = self.connections + 1
            print("Número de conexiones: ", self.connections)
            # except:
            # print("Error accepting connections")
   
    # #Constructor
    # def init(self):
    #     self.create_socket()
    #     self.bind_socket()
    #     self.accept_connections()
    
    #envio de mensajes, codificando el argumento pasado a binario    
    def send(self,con, data):
        data = data.encode('ascii')
        con.sendall(data)
        
    #recibo de mensajes, decodificando el mensaje desde binario, especificando el id del cliente   
    def rec(self, con):
        x =con.recv(1024)
        x=x.decode('ascii')
        return x
    
    #destructor
    #def __del__(self):
     #   for x in range(self.MAX):
      #      self.all_connections(x).close()
