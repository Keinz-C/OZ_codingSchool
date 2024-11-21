import socket

host = 'localhost'
port = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 서버쪽에 전화기를 놓은 것
server_socket.bind((host, port))    # 전화기를 기지국에 물린 것
server_socket.listen(5) # 통신의 옵션, 5명만 받겠다
server_socket.settimeout(5.0)   # 통신의 옵션, 5초후 자동종료


try:
    while True:
        print("Waiting for connection")
        client_socket, address = server_socket.accept()
        print("Got connection form", address)

        data = client_socket.recv(1024).decode("utf-8")
        print(data)
        client_socket.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        client_socket.close()
        print("Connection closed")
except Exception as e:
    print(e)
finally:
    server_socket.close()
