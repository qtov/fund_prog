class Response(object):
	"""Clasa care se ocupa de raspunsuri."""
	def __init__(self):
		self.__success = True
		self.resp_msg = []

	def add(self, type_, message):
		if (type_ == False):
			self.is_successful = False
		self.resp_msg.append(message)

	def display(self):
		for msg in self.resp_msg:
			print(msg)

	def is_successful(self):
		return self.__success

	def clear(self):
		del self.resp_msg
		self.resp_msg = [] 

