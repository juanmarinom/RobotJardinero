import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1',8000))
s.listen(1)
while True:
    conn,add=s.accept()
    # s.setblocking(1)
    data=conn.recv(1024)
    print(data)
    s.sendall('123-345-123')
    conn.close()
