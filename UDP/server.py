import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 12345))

while True:
    data, addr = s.recvfrom(4096)
    print(data.decode())
    s.sendto(bytes("Hello, this is UDP Server", 'utf-8'), addr)
