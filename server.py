import socket
import threading

ip_adress = '127.0.0.1'
port_number = 1234

THREADS = []
CMD_INPUT = []
CMD_OUTPUT = []

def handle_conection(connection, adress):
    msg = connection.recv(1024).decode()
    while msg != 'quit':
        print(msg)
        connection.send(msg.encode())
        msg = connection.recv(1024).decode()
    close_connection(connection)


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


if __name__ == "__main__":
    init_server()