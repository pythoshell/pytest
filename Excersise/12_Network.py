"""
You can create a simple client-server model for data exchange using Python.
Below are two Python scripts: one for the listener (server) and the other for the sender (client) to demonstrate a basic network communication model.


The server listens for incoming connections on the specified host and port.
The client connects to the server using the server's IP address or hostname and port.
The server receives data from the client and sends a response.
The client sends data to the server and displays the server's response.
The communication continues until the user enters "exit" in the client.
You should replace 'server_ip_or_hostname' in the client code with the actual IP address or hostname of the server.

Make sure to run the server script on one Windows system, and the client script on another, and they should be able to exchange data over the network.


"""

#Server (Listener) Python Code:


import socket

# Define the host and port on which the server will listen
host = '0.0.0.0'  # Listen on all available network interfaces
port = 12345

# Create a socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)
print(f"Server is listening on {host}:{port}")

# Accept an incoming connection
client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

while True:
    # Receive data from the client
    data = client_socket.recv(1024)  # Receive up to 1024 bytes of data
    if not data:
        break
    print(f"Received data from client: {data.decode()}")

    # Send a response back to the client
    response = "Data received successfully"
    client_socket.send(response.encode())

# Close the client and server sockets
client_socket.close()
server_socket.close()


#Client (Sender) Python Code:

import socket

# Define the server host and port
server_host = 'server_ip_or_hostname'  # Replace with the IP or hostname of the server
server_port = 12345

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_host, server_port))

while True:
    # Input data to send to the server
    data = input("Enter data to send (or 'exit' to quit): ")
    if data.lower() == 'exit':
        break

    # Send data to the server
    client_socket.send(data.encode())

    # Receive and print the server's response
    response = client_socket.recv(1024)
    print(f"Server response: {response.decode()}")

# Close the client socket
client_socket.close()


