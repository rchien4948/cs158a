from socket import *

serverName = input('Enter Server Name: ')
serverPort = input('Enter Server Port: ')

#TCP Socket Specs
clientSocket = socket(AF_INET, SOCK_STREAM)
#Connecting
clientSocket.connect((serverName, serverPort))


chat_message = input('Input sentence (in lowercase): ')
#Send message
clientSocket.send(chat_message.encode())