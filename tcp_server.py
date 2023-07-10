import socket
import json

HOST = '0.0.0.0'  # hostname or IP address
PORT = 5000  # specifying the PORT


def accept_client(client_socket):
    while True:
        data = client_socket.recv(1024)  # receive max 1024 bytes

        if not data:
            break  # if no more data , client has disconnected break the loop

        display = data.decode().strip()

        try:
            result = eval(display)
            response = {
                'data': result,
                'error': False
            }
        except:
            result = display
            response = {
                'data': result,
                'error': True
            }

        response_json = json.dumps(response)
        client_socket.sendall(response_json.encode())

    # close the connection if there's no data meaning that client has disconnected
    client_socket.close()


def start_server():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print("Server listening on {}:{}".format(HOST, PORT))

        while True:
            client_socket, client_address = server_socket.accept()
            print("Connected client : {}:{}".format(
                client_address[0], client_address[1]))
            # Connected client : 127.0.0.1:53344

            accept_client(client_socket)


start_server()
