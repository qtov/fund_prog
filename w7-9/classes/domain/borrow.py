class Borrow(object):
	def __init__(self, client, book):
		self.__client = client
		self.__book = book

	def getClient(self):
		return self.__client

	def getBook(self):
		return self.__book
	"""
	def __str__(self):
		return (self.__client.getName() + '(' + self.__client.getUid() + ') <- '
			self.__book.getTitle() + '(' + self.__book.getUid() + ')')
	"""

	def __str__(self):
		return ('Clientul ' + str(self.__client) + ' -> Cartea ' + str(self.__book) + '\n')

	def __eq__(self, borrow):
		if (self.getClient() == borrow.getClient() and self.getBook() == borrow.getBook()):
			return True
		else:
			return False
