import Server

server = Server.Server('192.168.137.1' , 31400)
server.send_message("Hello world")