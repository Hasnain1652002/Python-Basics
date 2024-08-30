## Python Server-Client Digit Summation Application

This project implements a server-client application using Python sockets. The client sends a string of digits to the server, which then sums the digits step-by-step until a single digit is obtained. The server sends each intermediate result back to the client for display.

## How It Works

1. **Server**:
   - Listens for incoming connections on a specified IP address and port.
   - Receives a string of digits from the client.
   - Sums the digits step-by-step until a single digit is obtained.
   - Sends each intermediate result back to the client.

2. **Client**:
   - Connects to the server using the specified IP address and port.
   - Sends a string of digits to the server.
   - Receives and displays each intermediate result from the server.

## Prerequisites

- Python 3.x installed on your machine.

## Step 1: Start the Server
Open a terminal or command prompt.
Navigate to the directory containing the server.py file.
Run the server using:

python server.py

## Step 2: Run the Client
Open a new terminal or command prompt.
Navigate to the directory containing the client.py file.
Run the client using:

python client.py

## Additional Notes
Both server and client can run on the same machine or different machines on the same network.
The server handles one client at a time and continues to run until manually stopped.