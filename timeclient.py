import socket

SIZE_OF_PART = 1024

class Client:
	def __init__(self, ip, port):
		self.connect(ip, port)

	def recieve(self):
		return self.sock.recv(SIZE_OF_PART).decode('UTF-8')

	def connect(self, ip, port):
		self.sock = socket.socket()
		self.sock.connect((ip, port))
		data = self.recieve() 
		print(data)

input_addres = input("Введите адрес сервера: ")
client = Client(input_addres, 1303)
