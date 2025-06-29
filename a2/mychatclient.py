from socket import *
import threading

serverName = input('Enter Server Name: ')
serverPort = int(input('Enter Server Port: '))

#TCP Socket Specs
clientSocket = socket(AF_INET, SOCK_STREAM)
#Connecting
clientSocket.connect((serverName, serverPort)) 
print("Connected to chat server. Type 'exit' to leave.")

def receive_messages():
    while True:
        try:
            message = clientSocket.recv(1024).decode()
            if not message:
                print("Disconnected from server.")
                break
            print(message)
        except:
            # print("Connection error.")
            break

def send_messages():
    while True:
        message = input()
        if message.lower() == "exit":
            print("Disconnected from Server")
            clientSocket.close()
            break
        try:
            clientSocket.send(message.encode())
        except:
            print("Failed to send message.")
            break

recv_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)

recv_thread.start()
send_thread.start()