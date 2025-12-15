#!/usr/bin/env python3

import socket
import json

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind(('localhost', 12345))

    server_socket.listen(1)

    while True:
        connection, client_address = server_socket.accept()

        try:
            data = connection.recv(1024)

            if data:
                received_dict = json.loads(data)
              
                print('Received Dictionary from Client:')
                print(received_dict)
        finally:
            connection.close()

def send_data(data_dict):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect(('localhost', 12345))

    try:
        serialized_data = json.dumps(data_dict)

        client_socket.sendall(serialized_data.encode())
    finally:
        client_socket.close()

def main():
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    time.sleep(1)

    sample_dict = {
        'name': 'Alice',
        'age': 30,
        'city': 'Paris'
    }
    send_data(sample_dict)

    server_thread.join()

if __name__ == "__main__":
    main()
