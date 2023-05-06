# Using socket library to create the interface
import socket

# The server's hostname or IP address
HOST = "127.0.0.1" 
# The port used by the server
PORT = 65432

# Create and work with the socket to send data to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect with the server
    s.connect((HOST, PORT))
    # Send the message "Hello World"
    s.sendall(b"Hello World")
    # Check to see that the data was received
    data = s.recv(1024)
# We should get back "Hello World" as it is just echoing what we say
print(f"Received {data!r}")
