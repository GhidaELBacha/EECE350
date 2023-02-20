from datetime import datetime
import time
import socket
import uuid
starttime = time.time()

host = socket.gethostname()
serverName = socket.gethostbyname(host)
serverPort = 2222
clientSocket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

#input of website IP address
websiteIP = input("Enter website IP : ")
#send IP address
clientSocket.send(websiteIP.encode())
#receive
response = clientSocket.recv(1024)

print ("From Server:", response.decode())


# Get the physical MAC address of the computer
print ("The MAC address in formatted way is : ", end="")
mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])

# Send  request to  proxy server and round-trip time
endtime = time.time()
roundtriptime = endtime - starttime

# Display the response and round-trip time
print("Response from website IP {websiteIP}:")
print(f"Round-trip time: {roundtriptime} seconds")

# Display physical MAC address
print(f"Physical MAC address: {mac_address}")


clientSocket.close()
