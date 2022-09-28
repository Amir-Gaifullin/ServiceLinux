import socket
from datetime import datetime

BUFFER = 1024

class Client:
	def __init__(self):
		self.__address = None
		self.__connection = None

	@property
	def address(self):
		return self.__address

	@address.setter
	def address(self, x):
		self.__address = x

	@property
	def connection(self):
		"""
		Returns:
			socket.socket: connection
		"""
		return self.__connection

	@connection.setter
	def connection(self, x):
		self.__connection = x

class Server:
	def __init__(self, ip, port):
		self.clients = set()
		self.sock = socket.socket()
		self.sock.bind((ip, port))

		self.listen()

	def listen(self):
		print('Start')
		self.sock.listen(2)
		while True:
			connection, address = self.sock.accept()

			client = Client()
			client.address = address
			client.connection = connection

			self.clients.add(client)

			print(f'Connected {address}')
			dateTime = datetime.now().strftime("%d.%m.%Y %H:%M")
			client.connection.send(dateTime.encode('UTF-8'))
			self.close_client(client)

	def close_client(self, client):
		self.clients.remove(client)
		client.connection.close()

server = Server('0.0.0.0', 1303)
