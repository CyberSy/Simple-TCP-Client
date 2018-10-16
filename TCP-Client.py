########## TCP client ############	
# python3 
# in python2 we don't need to send the data encoded (b)
import socket 

target_host = "127.0.0.1"
target_port = 4444

# create a soscker object 
client = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

# connect the client 
client.connect((target_host,target_port))

# send some data 

client.send(b"Hey! ")

# receive some data 

response = client.recv(4096)

print (response)
