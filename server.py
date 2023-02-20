from time import time  
import requests
import socket

# socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#  port
localhost =socket.gethostbyname(socket.gethostname())
# Bind the socket to the server address and port
serversocket.bind((localhost, 2222))
serversocket.listen(1)
while True:
        # Wait for a client connection
        client_socket, client_address = serversocket.accept()
        IP=client_socket.recv(1024)
        #print a message describing this request with the IP and exact time of the request
        print("the request is : ", IP.decode() )
        #second socket
        socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket2.connect((IP.decode(),80))
        request = "GET / HTTP/1.1\r\nHost:"+IP.decode()+"\r\n\r\n"
        #SEND TO DESTINATON SERVER
        print("request to destination ",request,"at time", datetime.utcnow())
        socket2.send(request.encode())
        recieveddata=socket2.recv(1024)
        FINALOUTPUT=client_socket.send(recieveddata)
       
        print("received data at time: ",datetime.utcnow())
        socket2.close()
        client_socket.close()
