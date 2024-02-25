import socket
import json
# import pygame
#
# clock = pygame.time.Clock
class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def create_server_socket(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.setblocking(0)
        self.server_socket.listen(2)

    def close_server_socket(self):
        self.server_socket.close()

    def open_socket(self, players_sockets):
        try:
            client_socket, client_address = self.server_socket.accept()
            client_socket.setblocking(0)
            players_sockets.append(client_socket)
            print(f"Подключение от {client_address}")
            return players_sockets
        except Exception as e:
            return players_sockets

    def get_message(self, sock):
        try:
            data = sock.recv(1024)
            data = data.decode()
            return data
            print(f"Получил {data}")
        except Exception as e:
            print(e)

    def send_message(self, sock, players_sockets):
        try:
            sock.send("Отправленное сообщение от сервера".encode())
            return players_sockets
        except Exception as e:
            print("1", players_sockets)
            #players_sockets.remove(sock)
            #sock.close()
            return players_sockets



