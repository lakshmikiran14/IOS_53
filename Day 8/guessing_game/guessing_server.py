'''
    Write a python server program that
        0. initialized a socket connection on localhost and port 10000
        1. accepts a connection from a  client
        2. receives a "Hi <name>" message from the client
        3. generates a random numbers and keeps it a secret
        4. sends a message "READY" to the client
        5. waits for the client to send a guess
        6. checks if the number is
            6.1 equal to the secret then it should send a message "Correct! <name> took X attempts to guess the secret"
            6.2 send a message "HIGH" if the guess is greater than the secret
            6.3 send a message "LOW" if the guess is lower than the secrent
        7. closes the client connection and waits for the next one
'''

import socket
import random as rd

s = socket.socket()
s.bind((socket.gethostname(),10000))
s.listen(5)

# while True:
# try:
clientsocket, address = s.accept()
inp = clientsocket.recv(20).decode()
if len(inp.split(" ")) > 1:
    name = inp.split(" ")[1]
print(inp)
secret = rd.randrange(0, 101, 1)
print("secret:", secret)
clientsocket.send(("READY").encode())
count = 1
while True:
    guess = int(clientsocket.recv(5).decode())
    print("guess:", guess)
    if guess > secret:
        clientsocket.send(("HIGH").encode())
        count += 1
    elif guess < secret:
        clientsocket.send(("LOW").encode())
        count += 1
    else:
        clientsocket.send(("Correct! " + name + " took " + str(count) + " attempts to guess the secret").encode())
        break
s.close()

