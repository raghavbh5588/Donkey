# echo-server.py

import socket

HOST = "100.84.40.97"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

BUFFER_SIZE = 20 #NOrmally 1024 but we want a fast response
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print("Connction address: ", addr)
while 1:
  data = conn.recv(BUFFER_SIZE)
  if not data: break
  print("received data: ", data)
conn.close()