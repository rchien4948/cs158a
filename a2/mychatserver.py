from socket import *
import threading
import time

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
print("Server now running on port", serverPort, ".")

threads = []