import socket
import datetime

# Define the IP address and port number to listen on
HOST = '172.16.1.175'
PORT = 12345

# Create a socket object and bind it to the specified IP address and port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

# Open a file for writing
with open('messages.txt', 'a') as f:
    f.write('Received messages:\n')

while True:

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
        message = data.decode().strip()
        print(f'Received: {message}')
        
        # Get the current date and time
        now = datetime.datetime.now()
        date_string = now.strftime('%Y-%m-%d')
        time_string = now.strftime('%H:%M:%S')

        # Write the message, date, time, and source IP address to the file
        with open('messages.txt', 'a') as f:
            f.write(f'{message}\t{date_string}\t{time_string}\t{addr[0]}\n')

        if message == 'END':
            break

    # Close the connection
    conn.close()
    
    if message == 'END':
        break

# Close the socket
s.close()
print('Server stopped.')
