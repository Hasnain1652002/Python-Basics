import os
import socket
from tqdm import tqdm

IP = socket.gethostbyname(socket.gethostname())
PORT = 4456
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
FILENAME = "friends-final.txt"
FILESIZE = os.path.getsize(FILENAME)

def main():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)

        data = f"{FILENAME}_{FILESIZE}"
        client.send(data.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"SERVER: {msg}")

        bar = tqdm(range(FILESIZE), f"Sending {FILENAME}", unit="B", unit_scale=True, unit_divisor=SIZE)

        with open(FILENAME, "rb") as f:
            while True:
                data = f.read(SIZE)

                if not data:
                    break

                client.send(data)
                msg = client.recv(SIZE).decode(FORMAT)

                bar.update(len(data))

        client.close()
        print("[+] File sent successfully.")
    except ConnectionRefusedError:
        print("[-] Error: The server is offline or cannot be reached.")
    except Exception as e:
        print(f"[-] An error occurred: {e}")

if __name__ == "__main__":
    main()
