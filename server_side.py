import socket
import threading

HOST = 'localhost'
PORT = 64231

def process_connection(sock, all_connections):
    while True:
        print(sock)
        print(addr)
        data = sock.recv(1024)  # размер (байт) ждем пока напишут
        print(data)
        decoded_data = data.decode('utf-8')  # декодируем
        print(decoded_data)
        # sock.sendall(data)  # эхо (отправляем сообщение себе)
        # another_sock.sendall(data)  # отправляем сообщение клиенту (другому)
        for conn in all_connections:
            conn.sendall(data)  # отправляем сообщение всем



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:  # создали object socket
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # теперь можем переиспользовать адрес
    server.bind((HOST, PORT))  # поднимаем сервер
    server.listen()  # сервер может читать

    connections = []

    while True:
            connection, addr = server.accept()  # ждем пока кто-то снаружи постучится по адресу (возвращает соединение и адрес)
            connections.append(connection)
            threading.Thread(target=process_connection, args=(connection, connections)).start()
        # another_connection, addr = server.accept()

    #  while True:
    #     print(addr)
    #     data = connection.recv(1024)  # размер (байт) ждем пока напишут
    #     print(data)
    #     decoded_data = data.decode('utf-8')  # декодируем
    #     print(decoded_data)
    #     connection.sendall(data)  # эхо
