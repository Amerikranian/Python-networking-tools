###UDP client
	#A simple wrapper over the socket module for creating a basic UDP client

import socket
class udp_client:
	def __init__(self, host, port, is_blocking, buffersize = 1024):
		#Please note: It is strongly recommended to pass False for is_blocking. The socket will freze otherwise and you will need to mess with threading
		self.host = host
		self.port = port
		self.socket_handler = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
		self.socket_handler.setblocking(is_blocking)

	def process_data(self, data):
		#This is called whenever data is received.
		return data

	def get_packet_data(self):
		#Tries to receive any data from the socket
		try:
			data = self.process_data(self.socket_handler.recvfrom(self.buffer_size))
			msg = data[0]
		except socket.error: return None

	def send_data(self, data):
		#Sends data to the current host and ports the socket is set to
		self.socket_handler.sendto(data, (self.host, self.port))

	def shutdown(self):
		#Shuts down the server. Must be called at the end of your program to avoid any issues arising with duplicate sockets
		self.socket_handler.close()