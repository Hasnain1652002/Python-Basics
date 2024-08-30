import socket
import sys

def start_client(server_ip='127.0.0.1', server_port=32000):
    """Connect to the server, send input, and display the server's response."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((server_ip, server_port))
            user_input = input("Enter String: ").strip()

            client_socket.sendall(user_input.encode('utf-8'))

            while True:
                response = client_socket.recv(1024).decode('utf-8')
                if not response:
                    break
                print(f"From Server: {response.strip()}")
    except ConnectionRefusedError:
        print("Error: Unable to connect to the server. Please ensure the server is running.")
    except Exception as e:
        print(f"Client encountered an error: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        start_client(sys.argv[1], int(sys.argv[2]))
    else:
        print("Usage: python client.py <server_ip> <server_port>")
        print("Using default server IP (127.0.0.1) and port (32000).")
        start_client()
