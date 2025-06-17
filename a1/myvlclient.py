from socket import *

serverName = 'localhost'
# serverName = input('Enter Server Name: ')
serverPort = 12000

#TCP Socket Specs
clientSocket = socket(AF_INET, SOCK_STREAM)
#Connecting
clientSocket.connect((serverName, serverPort))

message = input('Input sentence (in lowercase): ')
msg_len = len(message)
#assemble into full message sent:
msg_full = str(msg_len) + message
print("DEBUG: ", msg_full)
clientSocket.send(msg_full.encode())

mod_message = clientSocket.recv(64)
print("Server says: " + mod_message.decode())