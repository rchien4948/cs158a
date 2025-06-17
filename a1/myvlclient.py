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
#attach length indicator to front of sentence
if msg_len < 10: #padding length indicator as needed
    msg_len = "0"+str(msg_len)
else: msg_len = str(msg_len)
#assemble into full message sent:
msg_full = msg_len + message
# print("DEBUG: ", msg_full)

#Send message
clientSocket.send(msg_full.encode())

#Receive new message
mod_message = clientSocket.recv(64)
print("From server: " + mod_message.decode())