import socket


TCP_IP, TCP_PORT = '10.0.0.52', 5005 #Home address
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

print(1)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print('Connection address:'), addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print("received data:", data)
    conn.send(data)  # echo
conn.close()