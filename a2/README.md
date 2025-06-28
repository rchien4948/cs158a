# Chat Server with Multiple Clients
Based on the demo in class, you are going to build a chat server to which multiple clients can join to exchange messages.
The server program must maintain a list of connected clients and relay all messages to all active clients. (A message will NOT be relayed to the sender.)
A client can "exit" from the chat group at any time and must be removed from the client list of the server. (The client sends "exit" to the server. The exit message triggers the removal of the client from the list.)
Each message sent from a client to a server is a raw text input.
Each message sent from the server to a client should include (i) the client port number and (ii) the text message. Use the following format: f"{port_number}: {message}"
## Settings
For send and recv, you must use bufsize of 1024.
You must use TCP sockets.
The server waits for client connections at one port number.
Each client will establish a TCP socket connection when accepted and should be handled by a thread.
A user should be able to send text messages at any time and receive messages from other clients.
The server should keep waiting for a new client until it is terminated manually.
The client is terminated when the user inputs "exit".
## Notes
Assuming the message format (f"{port_number}: {message}"), make sure that your server works with any client implementation by your peers.
Also, your client program should be able to send and receive messages using another server implementation.
## Execution Example
### Server
    Server listening on 127.0.0.1:12345
    New connection from ('127.0.0.1', 51044)
    New connection from ('127.0.0.1', 51045)
    New connection from ('127.0.0.1', 51047)
    51044: Hi!
    51045: Hello!
    51047: How are you guys doing?
    51045: Good.
### Clients
Client 1

    Connected to chat server. Type 'exit' to leave.

    51044: Hi!
    Hello! # this is Client 1's input

    51047: How are you guys doing?
    Good. # this is Client 1's input
    exit
    Disconnected from server
Client 2

    Connected to chat server. Type 'exit' to leave.
    Hi! # this is Client 2's input

    51045: Hello!

    51047: How are you guys doing?

    51045: Good.
    exit
    Disconnected from server
Client 3

    Connected to chat server. Type 'exit' to leave.

    51044: Hi!

    51045: Hello!
    How are you guys doing? # this is Client 3's input

    51045: Good.
    exit
    Disconnected from server
## Submission Guide
Create a GitHub repo cs158a (This must be a public repo so I can clone it.)
Create a directory a2 under the cs158a repo
You should have three files in the a2 directory:
mychatclient.py: a client program
mychatserver.py: a server program
README.md: a brief explanation of how to run the programs. must include an execution example (copy, paste, and format the results shown on your terminals. It can be shown in the form of screenshots.)
Source codes should be appropriately commented. Also, we are going to check the modularity and readability of the code.
Submit the CLICKABLE URL to the github repo to Canvas.