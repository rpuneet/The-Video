

import socket

class Client:
    def __init__(self , host_ip , port):
        self.host = host_ip
        self.port = port

        self.socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

    def receive_file(self):
        self.socket.connect((self.host , self.port))
        print("Connected to server.")
        file_name = self.socket.recv(1024)

        with open(os.path.join(os.getcwd() , "Received_Files" , file_name) , 'wb') as file:
            print("File opened.")
            print("Receiving Data...")
            while True:
                data = self.socket.recv(1024)
                if not data:
                    break
                file.write(data.decode())
        file.close()





