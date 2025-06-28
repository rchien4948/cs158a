from socket import *
import threading
import time

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
print("Server now listening at:", serverPort, ".")

#For each new connection, start a new thread and print out connection message with IP and port of client
clients = []  # List of (conn, addr) tuples
clients_lock = threading.Lock()

def broadcast(message, sender_conn):
    with clients_lock:
        for conn, _ in clients:
            if conn != sender_conn: #send to all clients that didn't send the message
                try:
                    conn.send(message.encode())
                except:
                    pass 

def handle_client(conn, addr):
    with clients_lock:
        clients.append((conn, addr))
    print("New connection from:", addr)

    try:
        while True:
            message = conn.recv(1024).decode()
            if not message:
                break  # Client disconnected

            print(f"From {addr}: {message}")
            broadcast(message, sender_conn=conn)
    except Exception as e:
        print(f"Error with {addr}: {e}")
    finally:
        with clients_lock:
            clients.remove((conn, addr))
        conn.close()
        print(f"Connection closed: {addr}")


while True: #execution loop
    serverSocket.listen(1)
    conn_socket, addr = serverSocket.accept()
    client_thread = threading.Thread(target=handle_client, args=(conn_socket, addr)) #each client in its own thread
    client_thread.start()