

import socket

class Server:
    def __init__(self , host_ip , port):
        self.host = host_ip
        self.port = port

        self.socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

        self.socket.bind((self.host , self.port))

    def send_message(self , message):
        self.socket.listen(5)

        connection , address = self.socket.accept()

        connection.send(message.encode())
        connection.close()



