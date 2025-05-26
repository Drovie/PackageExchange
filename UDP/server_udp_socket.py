from socket import *


host = '192.168.43.235'
port = 6655
addr = (host,port)

udp_sock = socket(AF_INET, SOCK_DGRAM)
udp_sock.bind(addr)
print('Сервер успешно запущен!')


while True:
    message, addr = udp_sock.recvfrom(1024)
    if message != b'bye':
        print(addr[0], ':' ,port, '-->', message)
    else:
        udp_sock.close()
    
    messagefs = str.encode(input())
    udp_sock.sendto(messagefs, addr)
    
  
udp_socket.close()