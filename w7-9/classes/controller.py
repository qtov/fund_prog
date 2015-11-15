from classes.validator import Validator, re
from classes.book import Book
from classes.client import Client
from functions.utils import getMaxUid

class Controller(object):
	"""docstring for Controller"""
	def __init__(self, book_controller, client_controller):
		self.book = book_controller
		self.client = client_controller
	
	def __set_option(self, option):
		self.book.setOption(option)
		self.client.setOption(option)

	def __set_suboption(self, suboption):
		self.book.setSuboption(suboption)
		self.client.setSuboption(suboption)

	def take_option(self, option):
		Validator.validateOption(option, 1, 8)
		self.__set_option(int(option))

	def take_suboption(self, suboption):
		Validator.validateOption(suboption, 1, 2)
		self.__set_suboption(int(suboption))

class BookController(object):
	"""docstring for Controller"""
	def __init__(self, repository):
		self.__repository = repository

	def setOption(self, option):
		self.__option = option

	def setSuboption(self, suboption):
		self.__suboption = suboption
		
	def take(self, title, description, author):
		Validator.validateTitle(title)
		book = Book(getMaxUid('book') + 1, title, description, author)
		if (self.__option == 1):
			self.__repository.add(book)
		elif (self.__option == 2):
			pass
		elif (self.__option == 3):
			pass
		elif (self.__option == 4):
			pass
		elif (self.__option == 5):
			pass
		elif (self.__option == 7):
			pass

class ClientController(object):
	"""docstring for Controller"""
	def __init__(self, repository):
		self.__repository = repository

	def setOption(self, option):
		self.__option = option

	def setSuboption(self, suboption):
		self.__suboption = suboption

	def validateData(self, name, cnp):
		Validator.validateName(name)
		Validator.validateCNP(cnp)

	def take(self, name, cnp):
		self.validateData(name, cnp)
		client = Client(getMaxUid('client') + 1, name, cnp)
		if (self.__option == 1):
			self.__repository.add(client)
		elif (self.__option == 2):
			pass
		elif (self.__option == 3):
			pass
		elif (self.__option == 4):
			pass
		elif (self.__option == 5):
			pass
		elif (self.__option == 7):
			pass
