from socket import *


host = '192.168.43.235'
port = int(input())
addr = (host,port)

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)


messagefs = 0
message = 0

while message != 'bye'or messagefs != 'bye':
    message = str.encode(input())
    udp_socket.sendto(message, addr)

    messagefs = udp_socket.recvfrom(1024)
    if messagefs[0] != b'bye':
        print(addr, '-->', messagefs[0])
    else:
        break


udp_socket.close()

