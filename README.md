# File Transfer with Socket Programming

This project demonstrates a file transfer solution using socket programming. It consists of two programs: a server program and a client program. The server listens for incoming connections, and the client connects to the server to send a file. The server receives the file and saves it to its local filesystem.

## Server

### Features:
- Listens for incoming connections from clients.
- Receives the filename and filesize from the client.
- Uses the tqdm library to display progress while receiving the file.
- Handles timeouts when clients do not respond within 5 seconds.

### Usage:
1. Run the `server.py` script to start the server.
2. The server will wait for incoming connections.
3. Clients can connect to the server to send files.

## Client

### Features:
- Connects to the server using the server's IP address and port.
- Sends the filename and filesize to the server.
- Uses the tqdm library to display progress while sending the file.
- Handles the case when the server is offline or cannot be reached.

### Usage:
1. Modify the `FILENAME` variable in the `client.py` script to specify the file you want to send.
2. Run the `client.py` script to start the client.
3. The client will connect to the server and send the specified file.
4. You will receive confirmation messages regarding the transfer status.

## Additional Notes:
- Make sure both the server and client are running on the same network.
- Ensure that there are no firewall or network restrictions preventing communication between the server and client.
- The server's IP address and port number can be customized as needed.

For any questions or issues, please contact the project maintainers.

**Happy file transferring!**
