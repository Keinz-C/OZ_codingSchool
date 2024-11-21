import socket

host = "localhost"
port = 8000

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect((host, port))
send_data = b"hello"
my_socket.send(send_data)
print("send_data", send_data)
received_data = my_socket.recv(1024)
print("received_data", received_data)