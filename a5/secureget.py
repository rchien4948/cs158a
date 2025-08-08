from socket import *
import ssl

hostname = "www.google.com"
context = ssl.create_default_context()

with create_connection((hostname, 443)) as sock:
    #need a secure wrapper on sock
    with context.wrap_socket(sock, server_hostname=hostname) as sec_sock:
        request = f"GET / HTTP/1.1\r\nHost: {hostname}\r\nConnection: close\r\n\r\n"
        sec_sock.sendall(request.encode())