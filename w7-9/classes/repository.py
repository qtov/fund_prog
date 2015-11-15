from classes.book import Book
from classes.client import Client
from functions.utils import getMaxUid

class BookRepository(object):
	"""Repository"""
	def __init__(self):
		self.__list = []
		
	def getList(self):
		return self.__list

	def add(self, book):
		repository = open("repositories/book_repository", "a")
		repository.write(str(book))
		repository.close()

class ClientRepository(object):
	"""Client repository."""
	def __init__(self):
		self.__list = []

	def getList(self):
		return self.__list

	def add(self, client):
		repository = open("repositories/client_repository", "a")
		repository.write(str(client))
		repository.close()
