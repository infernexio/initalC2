import json
from mimetypes import init
import socket
import threading

ip_adress = 'localhost'
port_number = 9999

THREADS = []
CMD_INPUT = []
CMD_OUTPUT = []

def handle_conection(connection, adress):
   while True:
        commands=input("cmd>")
        if commands=='exit':
            return 0
        else:
            commands = bytes(commands, 'utf-8')
            connection.sendall(commands)
            out=connection.recv(64000).decode('utf-8')
            if out=="Dead":
                return 0
            else:
                print(out)


def close_connection(connection):
    connection.close()

def init_server():
    # creating socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip_adress, port_number))
    server_socket.listen(5)
    while True:
        connection,adress = server_socket.accept()
        # creating threads for each connectoin
        t = threading.Thread(target=handle_conection, args=(connection,adress))
        THREADS.append(t)
        t.start()
        t.join()


def main():
    init_server()


if __name__ == "__main__":
    main()