import socket
import threading

HOST = 'localhost'
PORT = 64231

def process_connection(sock, another_sock):
    while True:
        print(sock)
        print(addr)
        data = sock.recv(1024)  # размер (байт) ждем пока напишут
        print(data)
        decoded_data = data.decode('utf-8')  # декодируем
        print(decoded_data)
        sock.sendall(data)  # эхо
        another_sock.sendall(data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:  # создали object socket
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # теперь можем переиспользовать адрес
    server.bind((HOST, PORT))  # поднимаем сервер
    server.listen()  # сервер может читать

    connection, addr = server.accept()  # ожидаем пока кто-то снаружи постучится по адресу (возвращает соединение и адрес)
    another_connection, addr = server.accept()

    threading.Thread(target=process_connection, args=(connection, another_connection)).start()
    threading.Thread(target=process_connection, args=(another_connection, connection)).start()
    #  while True:
    #     print(addr)
    #     data = connection.recv(1024)  # размер (байт) ждем пока напишут
    #     print(data)
    #     decoded_data = data.decode('utf-8')  # декодируем
    #     print(decoded_data)
    #     connection.sendall(data)  # эхо
