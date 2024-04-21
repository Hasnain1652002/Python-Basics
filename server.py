import socket
from tqdm import tqdm

# Get the IP address of the local machine.
IP = socket.gethostbyname(socket.gethostname())
PORT = 4456  # Port number for the server
ADDR = (IP, PORT)  # Server address
SIZE = 1024  # Size of data chunks to be received from the client
FORMAT = "utf-8"  # Character encoding format

def main():
    try:
        # Create a TCP socket
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Bind the socket to the server address
        server.bind(ADDR)
        
        # Listen for incoming connections
        server.listen()
        print("[+] Listening...")

        # Set a timeout of 5 seconds for the connection
        server.settimeout(5)

        try:
            # Accept a client connection
            conn, addr = server.accept()
            print(f"[+] Client connected from {addr[0]}:{addr[1]}")

            # Receive the filename and filesize from the client
            data = conn.recv(SIZE).decode(FORMAT)
            item = data.split("_")
            FILENAME = item[0]
            FILESIZE = int(item[1])

            print("[+] Filename and filesize received from the client.")
            
            # Confirm the receipt of filename and filesize to the client
            conn.send("Filename and filesize received".encode(FORMAT))

            # Initialize a progress bar to display the file transfer progress
            bar = tqdm(range(FILESIZE), f"Receiving {FILENAME}", unit="B", unit_scale=True, unit_divisor=SIZE)

            # Open a file for writing the received data
            with open(f"recv_{FILENAME}", "wb") as f:
                while True:
                    data = conn.recv(SIZE)

                    # Break the loop when there's no more data to receive
                    if not data:
                        break

                    # Write the received data to the file
                    f.write(data)
                    
                    # Confirm the receipt of data to the client
                    conn.send("Data received.".encode(FORMAT))

                    # Update the progress bar
                    bar.update(len(data))

            # Close the connection
            conn.close()
            print("[+] File transfer complete.")
        except socket.timeout:
            # Handle a timeout, close the connection, and print a message
            print("[-] Client did not respond within 5 seconds. Connection closed.")
            server.close()
    except Exception as e:
        # Handle other exceptions and print an error message
        print(f"[-] An error occurred: {e}")

if __name__ == "__main__":
    main()
