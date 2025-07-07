from socket import *
import threading
import uuid
import sys
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.txt")
#First, open and read the config file
#The first line is the server address. Second line is the client address. 
def load_config():
    with open(CONFIG_PATH, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        if len(lines) != 2:
            print("config.txt must contain exactly 2 lines: server IP,port and client IP,port")
            sys.exit(1)
        server_ip, server_port = lines[0].split(",")
        client_ip, client_port = lines[1].split(",")
        return (server_ip.strip(), int(server_port.strip())), (client_ip.strip(), int(client_port.strip()))

(MY_IP, MY_PORT), (NEIGHBOR_IP, NEIGHBOR_PORT) = load_config()
MY_UUID = str(uuid.uuid4())
print(f"Initialized: [{MY_PORT}] UUID: {MY_UUID}")

class Message:
    def __init__(self, uuid_str, flag):
        self.uuid = uuid_str  # str
        self.flag = flag      # int

    def to_json(self):
        return json.dumps({'uuid': self.uuid, 'flag': self.flag})

    @staticmethod
    def from_json(data):
        d = json.loads(data)
        return Message(d['uuid'], d['flag'])
#Each process serves as client and server for another instance of process
