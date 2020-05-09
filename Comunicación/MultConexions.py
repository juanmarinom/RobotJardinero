import ServerClass
# import time

confC=0
confV=0
Ser = ServerClass.Server()
# while True:
    # time.sleep(0.5)
    # if(len(Ser.all_connections)>2):
print("Todos los clientes conectados, enviando informacion al control")
Ser.send(Ser.all_connections[0],'010-010-010')
# if...else
confC = Ser.rec(Ser.all_connections[0])
print ("Ha terminado el control, devolviendo: ", confC)
if confC!=0:
    print("Enviando informacion a la vision")
    while confV==0:
        Ser.send(Ser.all_connections[1],'Planta 1')
        confV=Ser.rec(Ser.all_connections[1])
        # if()
        # else
        print("Ha terminado la visión, devolviendo: ", confV)