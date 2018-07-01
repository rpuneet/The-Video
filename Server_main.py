import Server

host_ip = input("Enter Host ip : ")
port = int(input("Enter Port number : "))
file_path = input("Enter File Path : ")

server = Server.Server(host_ip , port)

server.send_file(file_path)