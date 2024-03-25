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

        data = client_socket.recv(1024)
        if data:
            client_socket.sendall(response)
        


if __name__ == "__main__":
    main()
