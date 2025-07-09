# The Leader Election Problem
This is an implementation of the Leader Election Problem, using the $O(n^2)$ algorithm. 

## Config.txt setup
Each config.txt should look like:
```    
10.1.1.1,5001
10.1.1.2,5001
```
where the first line is the IP/port used for the server portion, and the second line is where the process will look to connect as a client. 

## Setting up multiple nodes
Each node should be in its own folder. Each folder should contain a copy of myleprocess.py, config.txt, and log.txt. To have nodes connect to each other, ensure that the IPs/ports in config.txt point toward each other. 

## Running nodes
When running myleprocess.py, the program will wait for an 'Enter' keypress before the election begins. Once 'Enter' is pressed, you have 5 seconds (configurable) to initiate the election in any other nodes that you wish to run. Then, the election will be run, and information will be both printed to the terminal and written to each corresponding log.txt. The nodes should all exit on their own once the election is over. 

## Terminal Example:
    Initialized: [5001] UUID: 25917616-5d8b-44e0-acb1-a32324b13891
    [5001] Listening on 127.0.0.1:5001...
    [5001] Press Enter to initiate election (5 second countdown!)...

    [5001] Sent initial election message.
    [5001] Received: UUID=dc1be3d1-efcf-4d66-8cb9-0741bdf06e69, Flag=0
    [5001] Incoming UUID dc1be3d1-efcf-4d66-8cb9-0741bdf06e69 beats mine 25917616-5d8b-44e0-acb1-a32324b13891, forwarding!.
    [5001] Forwarded message UUID=dc1be3d1-efcf-4d66-8cb9-0741bdf06e69, Flag=0
    [5001] Received: UUID=dc1be3d1-efcf-4d66-8cb9-0741bdf06e69, Flag=1
    [5001] Leader already elected: dc1be3d1-efcf-4d66-8cb9-0741bdf06e69       
    [5001] Forwarded message UUID=dc1be3d1-efcf-4d66-8cb9-0741bdf06e69, Flag=1
    [5001] Received: UUID=dc1be3d1-efcf-4d66-8cb9-0741bdf06e69, Flag=1
    [5001] Leader already elected: dc1be3d1-efcf-4d66-8cb9-0741bdf06e69       
    [5001] Forwarded message UUID=dc1be3d1-efcf-4d66-8cb9-0741bdf06e69, Flag=1
    [5001] Final elected leader UUID: dc1be3d1-efcf-4d66-8cb9-0741bdf06e69
    [5001] Exiting...

## Log Example: 
    Sent: uuid=25917616-5d8b-44e0-acb1-a32324b13891, flag=0
    Received: uuid=dc1be3d1-efcf-4d66-8cb9-0741bdf06e69, flag=0, greater, 0
    Sent: uuid=dc1be3d1-efcf-4d66-8cb9-0741bdf06e69, flag=0
    Received: uuid=dc1be3d1-efcf-4d66-8cb9-0741bdf06e69, flag=1
    Leader determined to be dc1be3d1-efcf-4d66-8cb9-0741bdf06e69!
    Sent: uuid=dc1be3d1-efcf-4d66-8cb9-0741bdf06e69, flag=1
    Received: uuid=dc1be3d1-efcf-4d66-8cb9-0741bdf06e69, flag=1
    Leader determined to be dc1be3d1-efcf-4d66-8cb9-0741bdf06e69!
    Sent: uuid=dc1be3d1-efcf-4d66-8cb9-0741bdf06e69, flag=1
    Final elected leader UUID: dc1be3d1-efcf-4d66-8cb9-0741bdf06e69
