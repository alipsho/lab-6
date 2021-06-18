import math
import socket
import sys
import time
import errno
from multiprocessing import Process

def process_start(s_sock):
    s_sock.send(str.encode('CALCULATOR'))
    while True:
        data = s_sock.recv(2048)
        data = data.decode("utf-8")

        try:
            operation, val = data.split(":")
            opt = str(operation)
            n = float(val)

            if opt[0] == 'a':
                opt = 'Logarithm'
                ans = math.log10(n)
            elif opt[0] == 'b':
                opt = 'Square Root'
                ans = math.sqrt(n)
            elif opt[0] == 'c':
                opt = 'Exponential'
                ans = math.exp(n)
            else:
                answer = ('syntax error')

            sendAns = (str(opt)+ '['+ str(n) + ']= ' + str(ans))
            print ('\nanswer!!!')
        except:
            print ('Connection with client was ended...')
            sendAns = ('Connection with client was ended...')

        if not data:
            break

        s_sock.send(str.encode(str(sendAns)))
    s_sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",4444))
    print("Server is listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                print("Connected to the client...")
                p.start()

            except socket.error:

                print('There error in your socket connection')

    except Exception as e:
                print("An error occurred!")
                print(e)
                sys.exit(1)
    finally:
     	   s.close()
