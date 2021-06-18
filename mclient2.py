
import socket
import signal
import sys

c = socket.socket()
host = '192.168.56.102'
port =4444

print('Waiting for connection...')
try:
    c.connect((host, port))
except socket.error as e:
    print(str(e))

Response = c.recv(1024)
print(Response.decode("utf-8"))
while True:
    print("What mathematical function Do you want to use? :")
    print("Logarithm(a)")
    print("Square Root(b)")
    print("Exponential(c)")
    Input = input('\nEnter code here: ')

    if Input == 'a' or Input == 'b' or Input == 'c':
        n = input("Enter the number: ")
        Input = Input + ":" + n
        c.send(str.encode(Input))
        Response = c.recv(1024)
        print(Response.decode("utf-8"))

    elif Input == 'exit':
        break

    else:
        print("your functional code not available because the code is l,s,e and exit only....")
        c.send(str.encode(Input))
        Response = c.recv(1024)
        print(Response.decode("utf-8"))

c.close()
