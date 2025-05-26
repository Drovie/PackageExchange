
from termcolor import colored, cprint
import socket


def client_program():
    #host = socket.gethostname() 
    host = str(input())
    port = 5555  # номер порта серверного сокета

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # запрос на подключение к серверу
   
    cprint(('Connection to Server on ' + str(host) + ':' + str(port) + ' ' + 'has been established!'), 'green' ) # вывод сообщения об установлении соединения
    addr = client_socket.getsockname()
    message = input(" --> ")  # ввод сообщения для отправки серверу
    #message_info = '[User] ' + str(addr[0]) + ':' + str(port) + ' --> ' + message
    cprint(('[User]' + str(addr[0]) + '--> ' + message), 'yellow') # вывод отправляемого сообщения на экран


# while message - цикл (петля) передачи-получения сообщений между сервером и клиентом, разрывающийся от стоп-слова 'bye'
    while message.lower().strip() != 'bye': #Удаление пробелов перед сообщением и после него и переводит его в нижний регистр, проверяет со стоп-словом
        client_socket.send(message.encode())  # отправка сообщения посрдством сетевых буферов send
        data = client_socket.recv(1024).decode()  # получение ответа от сервера методом receive

        print('[Server] ' + str(host) + ':' + str(port) + ' --> ' + data)  # вывод полученного ответа на экран

        message = input(" -> ")  # ввод сообщения 
        #message_info = '[User] ' + str(addr[0]) +':' + str(addr[1])+ ' --> ' + message
        #message_info = '[User] ' + str(addr[0]) +':' + str(port)+ ' --> ' + message
        cprint(('[User] ' + str(addr[0]) + '--> ' + message), 'yellow') # вывод сообщения
       
    cprint(('Disconnected from server on ' + str(host) + ':' + str(port)), 'red') # вывод уведомления о разрыве соединения
    client_socket.close()  # разрыв соединения, удаление сокета


if __name__ == '__main__':
    client_program()