import socket

ip_adress = '127.0.0.1'
port_number = 1234

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((ip_adress, port_number))

msg = input("Enter msg to send :")

while msg != 'quit':
    client_socket.send(msg.encode())
    msg = client_socket.recv(1024).decode()
    print(msg)
    msg = input("Enter msg to send :")


client_socket.close()