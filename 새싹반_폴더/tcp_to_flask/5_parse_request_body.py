import socket

host = 'localhost'
port = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 서버쪽에 전화기를 놓은 것
server_socket.bind((host, port))    # 전화기를 기지국에 물린 것
server_socket.listen(5) # 통신의 옵션, 5명만 받겠다
server_socket.settimeout(5.0)   # 통신의 옵션, 5초후 자동종료

try:
    print("Waiting for connection")
    client_socket, address = server_socket.accept()
    print("Got connection from", address)

    data = client_socket.recv(1024).decode("utf-8")
    print(data)

    http_method_line = data.split("")[0]
    method, path, http_version = http_method_line.split(" ")
    print(f'method:{method}, path:{path}, http_version:h{http_version}')

   
    header_lines, body = data.split("\r\n\r\n")
    headers = header_lines.splitlines()[1:]

    response = None
    if method == 'GET' and path == '/':
        response = b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body>hi</body></html>\r\n "
    elif method == "GET" and path.startswith("/echo"):
        "/echo/hello"
        echo_value = path.split("/")[-1]
        response_string = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body>{echo_value}</body></html>\r\n "
        response = response_string.encode("euc-kr")
    elif method == "GET" and path == "/user_agent":
        "/user_agent"
        user_agent = None
        for header in headers:
            if "Iser-Agent" in header:
                user_agent = header
        response_string = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body>{user_agent}</body></html>\r\n "
        response = response_string.encode("euc-kr")
    elif method == "GET" and path == "/login":
        file_path = path(__file__).parent.absolute() / "login.html"
        response_body = None
        with open(file_path, "r") as f:
            response_body = f.read()
            headers = "\r\n".join([
                f"Content-Length: {len(response_body)}",
                "charset: utf-8"
            ])
            response_header = f"HTTP/1.1 200 OK\r\n{headers}\r\n\r\n".encode("euc-kr")
            response = response_header + response_body
    elif method == "POST" and path == "/login":
        print(body)
        response_body = body.encode("euc-kr")
        headers = "\r\n".join([
                f"Content-Length: {len(response_body)}",
                "charset: utf-8"
                ])
        response_header = f"HTTP/1.1 200 OK\r\n{headers}\r\n\r\n".encode("euc-kr")
        response = response_header + response_body
    # http프로토콜 버전 / \r\n은 줄바꿈 -> \r캐리지리턴 \n라인피드
    client_socket.send(response)  
    print("Connetion closed")
except Exception as e:
    print(e)
finally:
    server_socket.close()