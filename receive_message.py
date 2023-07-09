import socket
import json
import os

HOST = 'localhost'
PORT = 5000


def send_data(data):
    print("WORKING")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))  # Connect to the server
        client_socket.sendall(data.encode())  # Send the data to the server

        # Receive the response from the server
        response = client_socket.recv(1024)
        print(response)
        # Parse the received JSON response (parses into dictionary)
        print("WORKING")
        response_data = json.loads(response.decode())

        return response_data


def menu():
    # choice = ""

    # while choice != 'N' or choice != 'n':
    # default environment variable = 26+32
    data_to_send = str(os.getenv('DATA_TO_SEND', '26+32'))
    print(data_to_send)
    print("WORKING")
    response = send_data(data_to_send)

    if response:
        if response["error"] != "True":
            print("Result is: ", response["data"])
            print(response)
        elif response["error"] == "True":
            print("Wrong input, please try again.")

    # choice = input("Do you want to continue (Y/N) ?: ")


menu()

# To see which ports are in use (just to test)
# print(type(response))  # Process the received response (type = dictionary

# def scan_ports():
#     # Define the host (localhost) and the range of ports to scan
#     host = '127.0.0.1'  # Change to your desired host
#     start_port = 1
#     end_port = 65535

#     # Iterate over the range of ports and check if they are open
#     for port in range(start_port, end_port + 1):
#         # Create a socket object
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.settimeout(1)  # Set a timeout value for the connection attempt

#         # Attempt to connect to the port
#         result = sock.connect_ex((host, port))

#         # Check if the connection was successful (port is open)
#         if result == 0:
#             print(f"Port {port} is open")

#         # Close the socket
#         sock.close()


# # Call the function to scan ports
# scan_ports()
