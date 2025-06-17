from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
print("Server now running on port ", serverPort, ". \n")
while True:
    serverSocket.listen(1)

    conn_Socket, addr = serverSocket.accept()
    #accept client connection
    print("CONNECTED: ", str(addr))

    sentence = conn_Socket.recv(64).decode()
    new_sentence = sentence.upper()
    #uppercase sentence

    conn_Socket.send(new_sentence.encode())
    conn_Socket.close()