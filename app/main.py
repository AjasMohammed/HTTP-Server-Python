import socket, threading


def create_response(status_code, content_length, content, content_type="text/plain"):
    response = f"HTTP/1.1 {status_code}\r\nContent-Type: {content_type}\r\nContent-Length: {content_length}\r\n\r\n{content}".encode()
    return response


def handle_request(client_socket):
    response = b"HTTP/1.1 200 OK\r\n\r\n"
    with client_socket:
        bytes_data = client_socket.recv(1024)
        if bytes_data:
            data = bytes_data.decode().split("\r\n")
            path = data[0].split()[1]
            print("Data: ", data)
            if path == "/":
                pass
            elif path.startswith("/echo/"):
                content = path.replace("/echo/", "")
                response = create_response("200 OK", len(content), content)
            elif path.startswith("/user-agent"):
                content = data[2].split(":")[1].strip()
                response = create_response("200 OK", len(content), content)

            else:
                response = b"HTTP/1.1 404 Not Found\r\n\r\n"
        client_socket.send(response)


def main():
    print("Logs from your program will appear here!")
    host = "127.0.0.1"
    port = 4221

    with socket.create_server((host, port)) as server_socket:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address} has been established.")
            connection = threading.Thread(target=handle_request, args=(client_socket,))
            connection.start()


if __name__ == "__main__":
    main()
