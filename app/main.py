import socket, threading, argparse, os


def create_response(status_code, content_length, content, content_type="text/plain"):
    response = f"HTTP/1.1 {status_code}\r\nContent-Type: {content_type}\r\nContent-Length: {content_length}\r\n\r\n{content}".encode()
    return response


def check_file(directory, path):
    print('Current Directory: ', os.getcwd())
    print("Directory: ", directory)
    path = os.path.join(directory, path)
    print("Path: ", path)
    return os.path.exists(path)


def handle_request(client_socket, directory):
    response = b"HTTP/1.1 200 OK\r\n\r\n"
    not_found_status = b"HTTP/1.1 404 Not Found\r\n\r\n"
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
            elif path.startswith("/files/"):
                filename = path.replace("/files/", "")
                if check_file(directory, filename):
                    with open(os.path.join(directory, filename), "r") as file:
                        content = file.read()
                        print("Content: ", content)
                        response = create_response("200 OK", len(content), content, content_type='application/octet-stream')
                else:
                    response = not_found_status
            else:
                response = not_found_status
        client_socket.send(response)


def main():
    print("Logs from your program will appear here!")
    host = "127.0.0.1"
    port = 4221

    parser = argparse.ArgumentParser(description="HTTP Server")
    parser.add_argument("--directory", type=str, help="directory to serve", default=None)
    args = parser.parse_args()  # parse commandline arguments
    directory = args.directory

    with socket.create_server((host, port)) as server_socket:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address} has been established.")
            connection = threading.Thread(target=handle_request, args=(client_socket, directory))
            connection.start()


if __name__ == "__main__":
    main()
