# Using the socket library allows us to create an interface
import socket

 # Standard loopback interface address (localhost)
HOST = "127.0.0.1" 
# Port to listen on (non-privileged ports are > 1023)
PORT = 65432  

# Establish what socket needs to do
# In this case, what ever the server receives, 
# will be echoed back to the client
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Ties the socket to the network and port number
    s.bind((HOST, PORT))
    s.listen()
    # Accept the connection between server and client
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            # Data is sent and received between the client and server here
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)