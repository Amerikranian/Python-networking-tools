###UDP server
	#A simple wrapper over the socket module for creating a basic UDP server

import socket
class udp_server:
	def __init__(self, host, port, is_blocking = False, buffersize = 1024):
		#Please note: It is strongly recommended to pass False for is_blocking. The socket will freze otherwise and you will need to mess with threading
		self.host = host
		self.port = port
		self.buffer_size = buffersize
		self.socket_handler = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
		self.socket_handler.setblocking(is_blocking)
		self.socket_handler.bind((self.host, self.port))
		#A list of encountered clients
		self.client_list = []

	def process_data(self, data):
		#This is called whenever data is received.
		return data

	def get_packet_data(self):
		#Tries to receive any data from the socket
		try:
			data = self.process_data(self.socket_handler.recvfrom(self.buffer_size))
			msg = data[0]
			#Add client address to the list if it is not yet present
			if data[1] not in self.client_list: self.client_list.append(data[1])
			return msg
		except socket.error: return None

	def send_data(self, data, client):
		#Sends data to a specific client
		self.socket_handler.sendto(data, client)

	def send_to_all_clients(self, data):
		[self.send_data(data, a) for a in self.client_list]

	def shutdown(self):
		#Shuts down the server. Must be called at the end of your program to avoid any issues arising with duplicate sockets
		self.socket_handler.close()