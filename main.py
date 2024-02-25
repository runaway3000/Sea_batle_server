import time

from Classes import *
HOST = '127.0.0.1'
PORT = 5555

players_sockets = []

#Создаем подключение к серверу
server = Server(HOST, PORT)
server.create_server_socket()

running_server = True
while running_server:
    #Проверяем подключения и добавляем в players_sockets[]
    players_sockets = server.open_socket(players_sockets)
    for sock in players_sockets:

#        players_sockets = server.send_message(sock, players_sockets)
        try:
            print("Отправляем сообщение сообщение")
            sock.send("Отправленное сообщение".encode())
        except Exception as e:
            print("Ошибка 2", e)
            players_sockets.remove(sock)
            sock.close()



    #        data = server.get_message(sock)
        try:
            data = sock.recv(1024)
            data = data.decode()
            print(f"Получил: {data}")
        except Exception as e:
            print("Ошибка 1:", e)
    print()
    print()
    print()

    time.sleep(1)

server.close_server_socket()
