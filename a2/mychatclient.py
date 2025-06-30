from socket import *
import threading

serverName = input('Enter Server Name: ')
serverPort = int(input('Enter Server Port: '))

#TCP Socket Specs
clientSocket = socket(AF_INET, SOCK_STREAM)
#Connecting
try: 
    clientSocket.connect((serverName, serverPort)) 
    print("Connected to chat server. Type 'exit' to leave.")
except Exception as e:
    print(f"Error: Could not connect to {serverName}:{serverPort}.")    
    print(f"Reason: {e}")
    exit(1)

def receive_messages():
    while True:
        try:
            message = clientSocket.recv(1024).decode(errors='replace')
            if not message:
                print("Disconnected from server.")
                break
            # print(f"\r{message}\n> ", end='', flush=True)
            print(message + " \n> ", end='', flush=True) #attempt to fix formatting for if user is typing one message and receives a message in the middle of doing so. 
        except:
            # print("Connection error.")
            break

def send_messages():
    while True:
        message = input("> ")
        if message.lower() == "exit":
            print("Disconnected from Server")
            clientSocket.close()
            break
        if not message.strip():
            print("[WARNING] Cannot send empty message.")
            continue
        if len(message.encode()) > 1024:
            print("[Warning] Message too long. Limit to 1024 bytes.")
            continue
        try:
            clientSocket.send(message.encode())
        except:
            print("Failed to send message.")
            break

recv_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)

recv_thread.start()
send_thread.start()