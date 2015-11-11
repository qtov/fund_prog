class Response(object):
	"""docstring for Response"""
	def __init__(self):
		self.is_successful = True
		self.resp_msg = []

	def add(self, type_, message):
		if (type_ == False):
			self.is_successful = False
		self.resp_msg.append(message)

	
