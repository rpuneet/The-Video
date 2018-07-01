import Client

host = input("Enter Host ip : ")
port = input("Enter port : ")


client = Client.Client(host, port)
client.receive_file()