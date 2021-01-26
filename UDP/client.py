import socket

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = "Hello UDP"
c.sendto(msg.encode('utf-8'), ('localhost', 12345))
data, addr = c.recvfrom(4096)
print("Server Says")
data = data.decode()
print(data)
c.close()