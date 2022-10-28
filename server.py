import ipaddress
import socket
from xmlrpc import server

ip_adress = '127.0.0.1'
port_number = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((ip_adress, port_number))

server_socket.listen(2)

client_socket,adress = server_socket.accept()

print("Client: {}".format(adress))
msg = client_socket.recv(1024).decode()

while msg != 'quit':
    print(msg)
    client_socket.send(msg.encode())
    msg = client_socket.recv(1024).decode()


client_socket.close()
server_socket.close()