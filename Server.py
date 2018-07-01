

import socket

import os

class Server:
    def __init__(self , host_ip , port):
        self.host = host_ip
        self.port = port

        self.socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

        self.socket.bind((self.host , self.port))
        print("Server created.")
    def send_file(self , file_path):
        if not os.path.exists(file_path):
            raise Exception("File not found.")
        
        print("Waiting for connection.")

        self.socket.listen(5)

        connection , address = self.socket.accept()

        print("Connection received from - {}".format(address))

        with open(file_path , 'rb') as file:
            print("File Openned - {}".format(file_path))
            connection.send(os.path.basename(file_path).encode())
            print("Sending Data...")
            while(True):
                data = file.read(1024)
                if not data:
                    break
                connection.send(data)

        file.close()
        connection.close()



