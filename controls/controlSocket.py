import socket
import time

HOST = "100.113.29.118"  # The server's hostname or IP address
PORT = 3000  # The port used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
        s.sendall(b"0.849;-0.483")
        time.sleep(0.05)
        s.sendall(b"coocoo")
        time.sleep(0.05)
        s.sendall(b"cnom")
        time.sleep(0.05)