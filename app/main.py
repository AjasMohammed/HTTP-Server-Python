import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")
    host = '127.0.0.1'
    port = 4221
    response = b'HTTP/1.1 200 OK\r\n\r\n'

    with socket.create_server((host, port)) as server_socket:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} has been established.")

        bytes_data = client_socket.recv(1024)
        if bytes_data:
            data = bytes_data.decode().split('\r\n')
            path = data[0].split()[1]
            print('Path: ', path)
            if path == '/':
                pass
            elif path.startswith('/echo/'):
                content = path.replace('/echo/', '')
                response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(content)}\r\n\r\n{content}".encode()
            else:
                response = b'HTTP/1.1 404 Not Found\r\n\r\n'
        client_socket.send(response)
        


if __name__ == "__main__":
    main()
