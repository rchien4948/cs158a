# Variable-length message
Based on the demo in class, you are going to build client and server programs that can handle an arbitrary length of messages.
The message in this version has a number before the message text to tell the number of characters in the text.
The server program needs to keep handling the text until it sees the end of the message based on the specified length.

# Message Format
First n bytes of a message is the length of the message (In this assignment, you can assume n = 2 bytes)
When n = 2, you can assume that the text is between 1 character to 99 characters (All characters are between UTF8 U+0000 and U+007F.)

# Settings
For send and recv, you must use bufsize of 64.
You must use TCP sockets.
The server and client should use a single socket stream.
The server should keep waiting for a new client until it is terminated manually.
The client is terminated when it receives the complete sentence from the server.

# Server Function
Upon receiving a string from a client, it sends back the same string all in capital

# Output Example
Client side

Input lowercase sentence:10helloworld # This is a user input. 10 is the number of characters in the following sentence. (n = 2)
From Server: HELLOWORLD
Server side (Show some relevant information)

Connected from 10.0.0.2
msg_len: 10
processed: helloworld
msg_len_sent: 10
Connection closed
...

# Submission Guide
Create a GitHub repo cs158a (This must be a public repo so I can clone it.)
Create a directory a1 under the cs158a repo
You should have three files in the a1 directory:
myvlclient.py: a client program
myvlserver.py: a server program
README.md: a brief explanation of how to run the programs. must include an execution example (copy, paste, and format the results shown on your terminals. It can be shown in the form of screenshots.)
Source codes should be appropriately commented. Also, we are going to check the modularity and readability of the code.
Submit the CLICKABLE URL to the github repo to Canvas.