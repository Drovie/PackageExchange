#pip install termcolor
from termcolor import colored, cprint
import socket


def server_program():
    # get the host name - получения адреса устройства, на котором вызвана команда
    host = socket.gethostname() #мой адрес 
    port = 5555  # инициализация порта


    server_socket = socket.socket()  # создание (объявление) сетевого сокета
    server_socket.bind((host, port))  # инициализация адреса и порта сервера (соответствующего сокета)
    print('Server started') # вывод сообщения о начале работы сервера
    servaddr = server_socket.getsockname()
    server_socket.listen(10) # инициализация количества канаов связи
    conn, address = server_socket.accept()  # приём соединения 
    #(одобрение подключения к серверу, с другой стороны - запрос подключения)
    cprint (("[User] " + str(address[0]) + ' ' + 'has been connected!'), 'green')
    while True:
        data = conn.recv(1024).decode() # получение сообщения от клиента с помощью 
        #метода receive (размер буфера - 1024) и дешифрование
        print('[User] ' + str(address[0]) + '--> ' + data)
        if not data:
            # Условие (если данные (пакеты) не получены, то соединение разрывается)
            break 
        data = input(' -> ')
        cprint(('[Server] ' + str(servaddr[0]) + ':' + str(servaddr[1]) + '-->' + data), 'yellow')# вывод сообщения сервера на экран
        conn.send(data.encode())  # отправка сообщения (пакетов) клиенту с помощью метода send и дешифрование
    cprint(('User ' + str(host) + ' has been disconnected'), 'red') #вывод сообщения о разрыве соединения
    conn.close()  # разрыв соединения, удаление сокета


if __name__ == '__main__':
    server_program()