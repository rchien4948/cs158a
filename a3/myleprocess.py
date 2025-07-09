from socket import *
import threading
import uuid
import sys
import json
import os
import time

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

#Set some global states for each instance
received_uuids = set()
leader_uuid = None
leader_elected = threading.Event()

message_buffer = []       # list or Queue to hold Message objects
participated = False      # flag to indicate if initial election message was sent

#Message Handling
def handle_message(msg):
    global leader_uuid
    global participated

    print(f"[{MY_PORT}] Received: UUID={msg.uuid}, Flag={msg.flag}")

    if msg.flag == 1:
        print(f"[{MY_PORT}] Leader already elected: {msg.uuid}")
        leader_uuid = msg.uuid
        leader_elected.set()
        forward_message(msg)
        return

    if msg.uuid == MY_UUID:
        print(f"[{MY_PORT}] I am the leader!")
        leader_uuid = MY_UUID
        leader_elected.set()
        announce_leader()

    elif msg.uuid not in received_uuids:
        participated = True
        received_uuids.add(msg.uuid)
        forward_message(msg)
    else:
        print(f"[{MY_PORT}] Duplicate UUID {msg.uuid} ignored.")

def handle_connection(conn):
    try:
        data = conn.recv(1024).decode()
        conn.close()
        msg = Message.from_json(data)
        if not participated: #hasn't sent initial election message yet, hold received message for calculation later
            message_buffer.append(msg)
            print(f"[{MY_PORT}] Buffered message: UUID={msg.uuid}, Flag={msg.flag}")
        else: handle_message(msg) #initial election message WAS sent, proceed as usual
    except Exception as e:
        print(f"[{MY_PORT}] Connection handling error: {e}")
#The server thread
def server_thread():
    server = socket(AF_INET, SOCK_STREAM)
    # server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((MY_IP, MY_PORT))
    server.listen()
    print(f"[{MY_PORT}] Listening on {MY_IP}:{MY_PORT}...")

    while not leader_elected.is_set():
        try:
            conn, _ = server.accept()
            threading.Thread(target=handle_connection, args=(conn,), daemon=True).start() #hopefully fixes losing processes hanging
        except Exception as e:
            print(f"[{MY_PORT}] Server error: {e}")

def forward_message(msg):
    try:
        with socket(AF_INET, SOCK_STREAM) as s:
            s.connect((NEIGHBOR_IP, NEIGHBOR_PORT))
            s.sendall(msg.to_json().encode())
        print(f"[{MY_PORT}] Forwarded message UUID={msg.uuid}, Flag={msg.flag}")
    except Exception as e:
        print(f"[{MY_PORT}] Forwarding failed: {e}")

def announce_leader():
    msg = Message(MY_UUID, 1)
    forward_message(msg)

def initiate_election():
    global participated
    try:
        msg = Message(MY_UUID, 0)
        with socket(AF_INET, SOCK_STREAM) as s:
            s.connect((NEIGHBOR_IP, NEIGHBOR_PORT))
            s.sendall(msg.to_json().encode())
        print(f"[{MY_PORT}] Sent initial election message.")
        participated = True
        for buffered_msg in message_buffer:
            handle_message(buffered_msg)
        message_buffer.clear()
    except Exception as e:
        print(f"[{MY_PORT}] Could not connect to neighbor: {e}")

#-------------------------MAIN-------------------------------
if __name__ == "__main__":
    threading.Thread(target=server_thread, daemon=True).start()
    time.sleep(1)

    countdown = 5
    input(f"[{MY_PORT}] Press Enter to initiate election ({countdown} second countdown!)...\n")
    time.sleep(countdown) #press enter on ALL the instances within the countdown!
    initiate_election()

    try:
        while not leader_elected.is_set():
            time.sleep(0.5)
        print(f"[{MY_PORT}] Final elected leader UUID: {leader_uuid}")
        time.sleep(1)  # Give time for any last messages to be printed
    except KeyboardInterrupt: pass
    finally:
        print(f"[{MY_PORT}] Exiting...")
        sys.exit(0)