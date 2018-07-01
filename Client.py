

import socket

class Client:
    def __init__(self , host_ip , port):
        self.host = host_ip
        self.port = port

        self.socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

        self.socket.connect((self.host , self.port))

    def receive_message(self , message):
        data = self.socket.recv(1024)
        print(data)




