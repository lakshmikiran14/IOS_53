'''
    Write a python client program that
        0. connects to localhost and port 10000
        1. send a "Hi <name>" message
        2. waits for the server to send the "READY" message
        3. guess a number and send to the server
        4. wait for the server to send the message
        5. Read the message and make a decision based on the following
            4.1 Close the client if the message is of the form "Correct! <name> took X attempts to guess the secret"
            4.2 Use the clue given by the server and repeat from step 3
'''
import socket

# try:
s = socket.socket()
s.connect((socket.gethostname(),10000))

s.send(("Hi Lakshmi").encode())
resp = s.recv(10).decode()
lo = 0
hi = 100
if resp == "READY":
    while True:
        mid = (lo + hi)//2
        s.send(str(mid).encode())
        nresp = s.recv(100).decode()
        # print(nresp)
        if nresp == 'HIGH':
            hi = mid
        elif nresp == 'LOW':
            lo = mid
        else:
            print(nresp)
            break
s.close()
# except:
#     print("ERROR")
#     s.close()
