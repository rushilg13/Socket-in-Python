import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 12345))

while True:
    data, addr = s.recvfrom(4096)
    print(data)
    msg = bytes("Hello, this is UDP Server").encode('utf-8')
    s.sendto(msg, addr)
