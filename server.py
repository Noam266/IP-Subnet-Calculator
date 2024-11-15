import socket

# Setup server details
HOST = '127.0.0.1'  # Localhost, change to '' to listen on all network interfaces
PORT = 1246        # Port to listen on (use any free port above 1024)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket: 
  server_socket.bind((HOST, PORT))  # Bind the socket to the address and port
  server_socket.listen()            # Enable the server to accept connections
  print(f"🌐 Server is live on {HOST}:{PORT} - waiting for connections...")

#socket.socket(...) - creates a new socket object
#AF_INET - It specifies that this socket will use IPv4 addresses
#SOCK_STREAM - indicates that this socket will use the TCP protocol, which is connection-oriented and reliable

    while True:
        conn, addr = server_socket.accept()  # Wait for a client to connect
        with conn:
            print(f"🤖 Connected by {addr}")
            welcome_message = "Hello! please enter your data file."
            conn.sendall(welcome_message.encode())  # Send message to the client
            data = conn.recv(1024)  # Receive up to 1024 bytes from client
            if data:
                print(f"📩 Received from {addr}: {data.decode()}")  # Print client message





