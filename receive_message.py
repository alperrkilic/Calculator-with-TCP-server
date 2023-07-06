import socket
import json
import os

HOST = 'localhost'
PORT = 5000


def send_data(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))  # Connect to the server
        client_socket.sendall(data.encode())  # Send the data to the server

        # Receive the response from the server
        response = client_socket.recv(1024)
        # Parse the received JSON response (parses into dictionary)
        response_data = json.loads(response.decode())

        return response_data


def menu():
    # choice = ""

    # while choice != 'N' or choice != 'n':
    data_to_send = os.getenv("DATA_TO_SEND")
    response = send_data(data_to_send)

    if response:
        if response["error"] != "True":
            print("Result is: ", response["data"])
            # print(response)
        elif response["error"] == "True":
            print("Wrong input, please try again.")

    # choice = input("Do you want to continue (Y/N) ?: ")


menu()

# print(type(response))  # Process the received response (type = dictionary)
