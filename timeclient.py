import socket
from threading import Thread

SIZE_OF_PART = 1024

class Client:
	def __init__(self, ip, port):
		self.connect(ip, port)

	def recieve(self):
		return self.sock.recv(SIZE_OF_PART).decode('UTF-8')

	def read_socket(self):
		while True:
			data = self.recieve()
			print(data)
			break

	def loop(self):
		self.thread = Thread(target=self.read_socket)
		self.thread.start()

	def connect(self, ip, port):
		self.sock = socket.socket()
		self.sock.connect((ip, port))

		self.loop()

input_addres = input("Введите адрес сервера: ")
client = Client(input_addres, 1303)
client.loop()