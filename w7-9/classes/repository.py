from classes.book import Book
from classes.client import Client

class Repository(object):
	"""docstring for Repository"""
	def __init__(self):
		self.__book_list = []
		self.__client_list = []
		
	def getBookList(self):
		return self.__book_list

	def getClientList(self):
		return self.__client_list

	def getMaxUid(self, type_):
		max_uid = 0
		if (type_ == 'book'):
			for book in self.__book_list:
				if (book.getUid() > max_uid):
					max_uid = book.getUid()
		elif (type_ == 'client'):
			for client in self.__client_list:
				if (client.getUid() > max_uid):
					max_uid = client.getUid()
		else:
			raise NameError
		return max_uid

	def addBook(self, title, description):
		book = Book(self.getMaxUid('book') + 1, title, description)
		self.__book_list.append(book)
		for book in self.__book_list:
			print(book)

	def addClient(self, name, cnp):
		client = Client(self.getMaxUid('client') + 1, name, cnp)
		self.__client_list.append(client)
		for client in self.__client_list:
			print(client)


