from socket import *
import ssl
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, "response.html")

hostname = "www.google.com"
context = ssl.create_default_context()

with create_connection((hostname, 443)) as sock:
    #need a secure wrapper on sock
    with context.wrap_socket(sock, server_hostname=hostname) as sec_sock:
        request = f"GET / HTTP/1.1\r\nHost: {hostname}\r\nConnection: close\r\n\r\n"
        sec_sock.sendall(request.encode())

        response = b""
        while True:
            data = sec_sock.recv(4096)
            if not data:
                break
            response += data

with open(LOG_PATH, "a") as log_file:
    log_file.write(response.decode(errors="ignore"))

# print(response.decode(errors="ignore")) #DEBUG