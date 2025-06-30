# USAGE
First, start mychatserver.py. The default port is 12000. Then, start mychatclient.py instances as needed. Connect to the server program by entering 'localhost' for Server Name and '12000' (or whichever port, if you changed it in mychatserver.py) for Server Port. You can now start sending and receiving messages!

(Note: empty messages or messages of >1024 bytes will result in an error message!)

# Examples
## Server
    Server now listening at 0.0.0.0:12000
    New connection from: ('127.0.0.1', 55200)
    55200: Hello
    New connection from: ('127.0.0.1', 55206)
    55206: hello2

## Client 1
    Enter Server Name: localhost
    Enter Server Port: 12000
    Connected to chat server. Type 'exit' to leave.
    > Hello
    > 55206: hello2

## Client 2
    Enter Server Name: localhost
    Enter Server Port: 12000
    Connected to chat server. Type 'exit' to leave.
    > hello2