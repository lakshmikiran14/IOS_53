import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"connection from {address} has been established!")
    data = clientsocket.recv(20).decode("utf-8")
    print(data)
    clientsocket.send(bytes(data, "utf-8"))
