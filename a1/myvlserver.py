from socket import *
serverPort = 12000

def parse_packet(payload):
    #split payload into length and sentence
    sentence_len = int(payload[0] + payload[1])
    print("msg_length: ", sentence_len)
    sentence_content = payload[2:]
    print("processed: ", sentence_content)
    return sentence_content

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
print("Server now running on port", serverPort, ".")

while True:
    serverSocket.listen(1)
    conn_Socket, addr = serverSocket.accept()
    #accept client connection, show client IP
    print("CONNECTED: ", str(addr[0]))

    sentence = conn_Socket.recv(64).decode()
    parsed_input = parse_packet(sentence)
    new_sentence = parsed_input.upper()
    #uppercase sentence
    new_len = len(new_sentence)
    #track length for print output...

    conn_Socket.send(new_sentence.encode())
    print("msg_len_sent: ", new_len)
    conn_Socket.close()
    print("Connection Closed.\n")