# The Leader Election Problem
Any ambiguities must be reported and discussed on the discussion thread. (We want to experience the process of finding a "standard" implementation of a custom application protocol.)

 

## What is The Leader Election Problem?
In distributed computing, leader election is the process of designating a single process as the organizer of some task distributed among several computers (nodes).
## Definition
A valid leader election algorithm must meet the following conditions:

Termination: the algorithm should finish within a finite time once the leader is selected.
Uniqueness: there is exactly one process that considers itself as leader.
Agreement: all other processes know who the leader is.
## Generating Unique ID
A Universally Unique Identifier (UUID) is a 128-bit label used for identification in computer systems.
When generated according to the standard methods, UUIDs are, for practical purposes, unique.
We are going to use the ```uuid.uuid4()``` method to decide an ID of a process
## Node Configuration
We assume an asynchronous non-anonymous ring.
Each node has exactly two neighbors.
Your code should include both client and server functionalities.
As a server, you will wait for another node to connect to your node.
As a client, you will connect to another node.
You will exchange a pair of IP address and port number outside of the code in class.
You prepare a simple text file config.txt in the same directory as the code. The configuration file should look like:
    ```10.1.1.1,5001
    10.1.1.2,5001```
The first line should include your IP address (as a server).
The second line is the info exchanged with another student (as a client).
When you run the code, the configuration file should be used to initialize the connections. (You may want to set a reasonable length of sleep time to wait for a server node to be up.)
## Connection
Once you establish a socket connection, please maintain the connection between the neighbors for further communications. (Do not accept or ask for a new connection.)
## Multithreading
When you accept a connection, the server process needs to be run in a separate thread.
This is because, if the single thread program has accept and connect in a sequence (as follows), there is no one to start the client connection, while waiting as a server with the accept
    1: server.accept()
    2: client.connect()
After a connection is established, you can use single threading (or keep the multiple threads with a shared memory).
## Algorithm
Your node performs the $O(n^2)$ algorithm.
Read the first two paragraphs under under the Asynchronous ring sectionLinks to an external site. in the Wikipedia reference article.
Sending direction
We decide the direction of the ring based on the client-server relationship.
You can assume that a message is always sent from a client to the corresponding server.
You should receive messages as a server and send messages as a client.
Once you, as a client, are connected to a server, you should send a message with your uuid (without any comparison) as the initial message. This only happens once.

## Message Format
You must define a Message class, which have two member variables:
uuid.UUID uuid: indicating the sender's UUID. Note: This ID should be the same throughout the leader election process. (e.g. 123e4567-e89b-42d3-a456-556642440000)
int flag: representing if the leader is already elected.
0 if it is still in the process of leader election (initial value).
1 if a leader is already elected.
As discussed in class, we use use JSON to serialize the Message instances. Do not change the aforementioned variable names.

## Termination
When enough time passes, every node in the ring (including your node) should have stopped sending messages (Termination condition) and had the same ID in a member variable named leader_id (Uniqueness and Agreement conditions).
When terminating, the node should print something like "leader is <leader_id>"
## Log
When a process receives a message, it should clearly show, on a log file log.txt,
"Received"
uuid in the message
flag
if the message's uuid is greater than the process's uuid(print greater, same, or less).
if this process is in state 0 (still trying to find a leader) or state 1 (it knows the leader's ID).
If it is in state 1, show the leader's ID
When a process ignores the message, it should clearly show, on a log file, that the received message was ignored.
When a process sends a message, it should clearly show, on a log file,
"Sent"
uuid in the message
flag
    ```Received: uuid=f81d4fae-7dec-11d0-a765-00a0c91e6bf6, flag=0, less, 0
    Received: uuid=f81d4fae-dddd-11d0-a765-00a0c91e6bf6, flag=0, greater, 0
    Sent: uuid=f81d4fae-dddd-11d0-a765-00a0c91e6bf6, flag=0```
    ...
    ...
    ```Leader is decided to f81d4fae-dddd-11d0-a765-00a0c91e6bf6.
    Sent: uuid=f81d4fae-dddd-11d0-a765-00a0c91e6bf6, flag=1```
...
## Demo
Using three duplicates of your process implementation, create a ring and execute the election process.
## Submission Guide
Create a directory a3 under the cs158a repo
You should have the following files in the a3 directory:
myleprocess.py: the process to be part of the election ring
config.txt: the aforementioned config file
log1.txt, log2.txt, log3.txt: log files from the three processes in your local demo
README.md: a brief explanation of how to run the programs. must include an execution example (copy, paste, and format the results shown on your terminals. It can be shown in the form of screenshots.)
Source codes should be appropriately commented. Also, we are going to check the modularity and readability of the code.
Submit the CLICKABLE URL to the github repo to Canvas.