import socket

# Define the IP address and port number to listen on
HOST = '172.16.1.175'
PORT = 12345

# Create a socket object and bind it to the specified IP address and port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

# Set the socket to listen for incoming connections
s.listen(1)
print('Waiting for a connection...')

# Wait for a client to connect
conn, addr = s.accept()
print(f'Connected by {addr}')

# Receive data from the client
while True:
    
    data = conn.recv(1024)
    if not data:
        break
    print(f'Received: {data.decode()}')
    
# Close the connection
conn.close()
