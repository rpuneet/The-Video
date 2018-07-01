import Client

client = Client.Client("192.168.43.1" , 31400)
print(client.receive_message(1024))