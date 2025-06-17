# Running programs:
First, run myvlserver.py in a terminal. This will run the server program on localhost, at port 12000. Then, run myvlclient.py, and enter a sentence to send to the server. Client program will exit when a sentence is sent and received. Server will continuously listen for client connections until manually terminated. 

# Execution Example: 
## Server side:
    Server now running on port 12000 .
    CONNECTED:  127.0.0.1
    msg_length:  10
    processed:  helloworld
    msg_len_sent:  10
    Connection Closed.
## Client side:
    Input sentence (in lowercase): helloworld
    From server: HELLOWORLD