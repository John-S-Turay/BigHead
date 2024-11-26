import socket
import subprocess

# Creates a socket, binds it to the specified host and port, and listens for incoming connections.
def create_socket():
    host = "127.0.0.1"
    port = 9000
    s = socket.socket()
    s.bind((host, port))
    s.listen(5)
    print("Waiting for client connection")
    return s

# Sends commands to the connected client and receives the output.
def send_commands(conn):
    while True:
        cmd = input("Enter command: ")
        if cmd == 'quit' or 'exit' :
            conn.close()
            break
        conn.sendall(cmd.encode())
        output = conn.recv(1024).decode()
        print(output, end='')

# Main function to create a socket, accept connections, and send commands.
def main():
    server_socket = create_socket()
    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")
    send_commands(conn)

if __name__ == "__main__":
    main()