import socket

def sum_digits_step_by_step(num_str):
    """Generate and yield the sum of digits step-by-step until a single digit is obtained."""
    while len(num_str) > 1:
        total = sum(int(digit) for digit in num_str)
        yield total
        num_str = str(total)

def start_server(host='127.0.0.1', port=32000):
    """Start the server and listen for incoming client connections."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server is running at {host}:{port}...")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024).decode('utf-8')

                if not data.isdigit():
                    response = "Sorry, Numbers required"
                    conn.sendall(response.encode('utf-8'))
                else:
                    # Send each step of the sum process
                    for result in sum_digits_step_by_step(data):
                        conn.sendall(f"{result}\n".encode('utf-8'))
                        print(f"Sent: {result}")

if __name__ == "__main__":
    start_server()
